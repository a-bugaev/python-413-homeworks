"""
hw_37/peewee_db/__init__.py
"""

from .models import (
    Master,
    Service,
    Appointment,
    MasterService,
    AppointmentService,
)
from .utils import (
    create_tables,
    populate_db,
    check_db_file_existance,
    check_tables_existance,
    remove_db_file,
)
