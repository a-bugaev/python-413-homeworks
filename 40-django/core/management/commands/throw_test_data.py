"""
core/test_data.py

Populates DB with example data for development, testing and demonstration purposes
"""

import os
import json
import pathlib
import random
import datetime

import requests
import tqdm

from django.core.management.base import BaseCommand
from django.core.files.images import ImageFile
from django.conf import settings
from django.utils import timezone
from core.models import (  # type: ignore  # pylint: disable=import-error
    Order,
    Master,
    Service,
    Review,
    DecorImage,
)


class Command(BaseCommand):
    """
    Populates DB with example data for development, testing and demonstration purposes
    """

    help = "Populates DB with example data for development, testing and demonstration purposes"

    def __init__(self):
        super().__init__()
        self.google_drive_url_ = {}
        self.pics_ids_ = {}
        self.masters_ = {}
        self.services_ = {}
        self.orders_ = {}
        self.reviews_ = {}

    def load_data(self):
        """
        data taken off to json for readability, now read them
        """
        with open(
            pathlib.Path(__file__).resolve().parent / "data.json", "r", encoding="utf-8"
        ) as f:
            return json.loads(f.read())

    def download_pics(self):
        """
        Downloads images from googledrive to media/ dir
        """
        print("downloading pics...")
        total = sum([len(dir_) for dir_ in self.pics_ids_.values()])
        pbar = tqdm.tqdm(total=total)
        for dir_name, content_dict in self.pics_ids_.items():
            for file_name, file_id in content_dict.items():
                filepath = pathlib.Path(settings.MEDIA_ROOT / dir_name / f"{file_name}.webp")
                filepath.parent.mkdir(parents=True, exist_ok=True)
                if not filepath.is_file():
                    response = requests.get(self.google_drive_url_.format(file_id), timeout=5)
                    if response.status_code == 200:
                        with open(filepath, "wb") as f:
                            f.write(response.content)
                pbar.update(1)
        pbar.close()

    def remove_pics(self):
        """
        django creates copy of each pic undef new unique name, so we remove originals
        """
        for dir_name, content_dict in self.pics_ids_.items():
            for file_name, _ in content_dict.items():
                os.remove(settings.MEDIA_ROOT / dir_name / f"{file_name}.webp")

    def _add_services(self):
        for i, service in enumerate(self.services_, start=1):
            rel_file_path = (settings.MEDIA_ROOT / "service" / f"{i}.webp").relative_to(
                settings.BASE_DIR
            )
            Service(
                id=i,
                name=service["name"],
                description=service["description"],
                price=service["price"],
                duration=random.randint(10, 300),
                image=ImageFile(open(rel_file_path, "rb"), name=f"{i}.webp"),
            ).save()

    def _add_masters(self):
        for i, master in enumerate(self.masters_, start=1):
            rel_file_path = (settings.MEDIA_ROOT / "master" / f"{i}.webp").relative_to(
                settings.BASE_DIR
            )
            inst = Master(
                id=i,
                name=master["name"],
                bio=master["description"],
                photo=ImageFile(open(rel_file_path, "rb"), name=f"{i}.webp"),
                experience=master["work_experience"],
            )
            inst.save()
            inst.services_provided.set([Service.objects.get(id=id_) for id_ in master["services"]])

    def _add_orders(self):
        for order in self.orders_:
            inst = Order(
                client_name=order["client_name"],
                phone="".join(random.choices([str(n) for n in range(10)], k=11)),
                master=Master.objects.get(id=order["master_id"]),
                appointment_date=timezone.make_aware(
                    datetime.datetime.combine(
                        datetime.datetime.strptime(order["date"], "%Y-%m-%d").date(),
                        datetime.time(random.randint(10, 20), 0, 0),
                    )
                ),
                status=order["status"]
            )
            inst.save()
            inst.services.set([Service.objects.get(id=id_) for id_ in order["services"]])

    def _add_reviews(self):
        for review in self.reviews_:
            inst = Review(
                text=review["text"],
                client_name=review["client_name"],
                master=Master.objects.get(id=review["master"]),
                rating=review["rating"],
            )
            inst.save()
            inst.services_were_provided.set(
                [Service.objects.get(id=id_) for id_ in review["services"]]
            )

    def _add_decor_images(self):
        for name in self.pics_ids_["decor"].keys():
            rel_file_path = (settings.MEDIA_ROOT / "decor" / f"{name}.webp").relative_to(
                settings.BASE_DIR
            )
            DecorImage(
                image=ImageFile(open(rel_file_path, "rb"), name=f"{name}.webp"), name=name
            ).save()

    def populate_db(self):
        """
        manually adds data to db
        """
        self._add_services()
        self._add_masters()
        self._add_orders()
        self._add_reviews()
        self._add_decor_images()

    def clear_db(self):
        """
        erase everything before population
        """
        for model in [
            Order,
            Master,
            Service,
            Review,
            DecorImage,
        ]:
            model.objects.all().delete()

    def handle(self, *args, **options):
        (
            self.google_drive_url_,
            self.pics_ids_,
            self.masters_,
            self.services_,
            self.orders_,
            self.reviews_,
        ) = self.load_data().values()
        self.clear_db()
        self.download_pics()
        self.populate_db()
        self.remove_pics()
