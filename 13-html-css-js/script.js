
const geocodeMapsCoApiReverseUrl = "https://geocode.maps.co/reverse";
// ?q=address&api_key=api_key
const geocodeMapsCoApiForwardUrl = "https://geocode.maps.co/search";
// "?lat=latitude&lon=longitude&api_key=api_key"
const geocodeMapsCoApiKey = "67206f61b830e500180237pxnff455c";

const openWeatherMapApiUrl = "https://api.openweathermap.org/data/2.5/weather";
// ?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API key}
const openWeatherMapAPIKey = "c0b78f31b171637ff76f0d0beab25c85";

var inputDelayTimer = null;

const fetchListOfCities = async (query) => {
  const response = await fetch(
    `${geocodeMapsCoApiForwardUrl}/?q=${query}&api_key=${geocodeMapsCoApiKey}`
  );
  const data = await response.json();
  return data;
};

const fetchWeather = async (coords) => {
  const response = await fetch(
    `${openWeatherMapApiUrl}?` +
    `lon=${coords.lon}&` +
    `lat=${coords.lat}&` +
    `exclude=minutely,hourly,daily,alerts&` +
    `units=metric&` +
    `lang=RU&` +
    `appid=${openWeatherMapAPIKey}`
  );
  const data = await response.json();
  return data;
};

const fetchAirQualityData = async (coords) => {
  const response = await fetch(
    `https://api.openweathermap.org/data/2.5/air_pollution?` +
    `lon=${coords.lon}&` +
    `lat=${coords.lat}&` +
    `appid=${openWeatherMapAPIKey}`
  );
  const data = await response.json();
  return data;
};

const handleSearch = async (query) => {
  if (!query) { return }
  let data = await fetchListOfCities(query);
  document.querySelector(".searchPromptsContainer").innerHTML = "";
  data.forEach((place) => {
    promptEl = document.createElement("p");
    promptEl.innerHTML = place.display_name;
    promptEl.className = "searchPrompt";
    promptEl.addEventListener("click", handleSearchPromptClick);
    promptEl.id = place.place_id;
    promptEl.place = place;
    document.querySelector(".searchPromptsContainer").appendChild(promptEl);
  });
  cities = data;
};

handleSearchPromptClick = async (e) => {
  document.getElementById("searchInput").value = e.target.innerHTML;
  document.querySelector(".searchPromptsContainer").innerHTML = "";

  let coords = {
    lat: e.target.place.lat,
    lon: e.target.place.lon,
  };

  let weatherData = await fetchWeather(coords);
  let airQualityData = await fetchAirQualityData(coords);
  showWeather(weatherData, airQualityData);
};

function showWeather(weatherData, airQualityData) {

  console.log(airQualityData);

  const markup = `
    <div class="row" id="">
      <div class="col-12">
        <div class="card my-3">
          <div class="row">
            <div class="col-4">
              <img class="card-img-top picture" alt="weather picture">
            </div>
            <div class="col-8">
              <div class="card-body d-flex flex-column flex-wrap" style="height: 512px">
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  `;

  const fields = [
    "location",
    "weatherName",
    "date",
    "sunrise",
    "sunset",
    "timeZone",
    "tempMax",
    "tempItself",
    "feelsLike",
    "tempMin",
    "humidity",
    "pressure",
    "windSpeed",
    "windDirection",
    "co",
    "no",
    "no2",
    "o3",
    "so2",
    "pm2_5",
    "pm10",
    "nh3"
  ];

  const id = `id_${Date.now()}`;

  document.getElementById("weatherContainer").innerHTML = markup.replace(
    `id=""`,
    `id="${id}"`
  );

  let valueElements = {};

  fields.forEach((field) => {
    let el = document.createElement("p");
    el.id = `${id}_${field}`;
    el.className = "card-text w-25";
    document.querySelector(`#${id} .card-body`).append(el);
    valueElements[field] = el;
  });

  valueElements.location.innerHTML = weatherData.name;

  valueElements.date.innerHTML =
    '<i class="bi bi-calendar"></i>&nbsp;&nbsp;' +
    new Date(weatherData.dt * 1000).toLocaleDateString();

  valueElements.sunrise.innerHTML =
    '<i class="bi bi-sunrise"></i>&nbsp;&nbsp;' +
    new Date(weatherData.sys.sunrise * 1000).toLocaleTimeString();

  valueElements.sunset.innerHTML =
    '<i class="bi bi-sunset"></i>&nbsp;&nbsp;' +
    new Date(weatherData.sys.sunset * 1000).toLocaleTimeString();

  valueElements.timeZone.innerHTML =
    '<i class="bi bi-clock"></i>&nbsp;&nbsp;UTC&nbsp;' +
    (weatherData.timezone > 0 ? "+" : "") +
    weatherData.timezone / 3600;

  valueElements.tempMax.innerHTML =
    "maximum " +
    (weatherData.main.temp_max > 0 ? "+" : "") +
    Math.round(weatherData.main.temp_max) +
    " °C";

  valueElements.tempItself.innerHTML =
    "current " +
    (weatherData.main.temp > 0 ? "+" : "") +
    Math.round(weatherData.main.temp) +
    " °C";

  valueElements.feelsLike.innerHTML =
    "( feels like " +
    (weatherData.main.feels_like > 0 ? "+" : "") +
    Math.round(weatherData.main.feels_like) +
    " °C)";

  valueElements.tempMin.innerHTML =
    "minimum " +
    (weatherData.main.temp_min > 0 ? "+" : "") +
    Math.round(weatherData.main.temp_min) +
    " °C";

  valueElements.humidity.innerHTML =
    '<i class="bi bi-droplet"></i> ' + weatherData.main.humidity + "%";

  valueElements.pressure.innerHTML =
    Math.round((weatherData.main.pressure * 100) / 133.3) + " мм.рт.ст.";

  valueElements.windSpeed.innerHTML =
    '<i class="bi bi-wind"></i> ' + weatherData.wind.speed + " м/с";

  let hRWindDirection = "";
  switch (true) {
    case weatherData.wind.deg >= 337.5 || weatherData.wind.deg <= 22.5:
      hRWindDirection = "С";
      break;
    case weatherData.wind.deg >= 22.5 && weatherData.wind.deg <= 67.5:
      hRWindDirection = "СВ";
      break;
    case weatherData.wind.deg >= 67.5 && weatherData.wind.deg <= 112.5:
      hRWindDirection = "В";
      break;
    case weatherData.wind.deg >= 112.5 && weatherData.wind.deg <= 157.5:
      hRWindDirection = "ЮВ";
      break;
    case weatherData.wind.deg >= 157.5 && weatherData.wind.deg <= 202.5:
      hRWindDirection = "Ю";
      break;
    case weatherData.wind.deg >= 202.5 && weatherData.wind.deg <= 247.5:
      hRWindDirection = "ЮЗ";
      break;
    case weatherData.wind.deg >= 247.5 && weatherData.wind.deg <= 292.5:
      hRWindDirection = "З";
      break;
    case weatherData.wind.deg >= 292.5 && weatherData.wind.deg <= 337.5:
      hRWindDirection = "СЗ";
      break;
  }

  valueElements.co.innerHTML = "CO " + airQualityData.list[0].components.co + " μg/m3";
  valueElements.no.innerHTML = "NO " + airQualityData.list[0].components.no + " μg/m3";
  valueElements.no2.innerHTML = "NO2 " + airQualityData.list[0].components.no2 + " μg/m3";
  valueElements.o3.innerHTML = "O3 " + airQualityData.list[0].components.o3 + " μg/m3";
  valueElements.so2.innerHTML = "SO2 " + airQualityData.list[0].components.so2 + " μg/m3";
  valueElements.pm2_5.innerHTML = "PM 2.5 " + airQualityData.list[0].components.pm2_5 + " μg/m3";
  valueElements.pm10.innerHTML = "PM 10 " + airQualityData.list[0].components.pm10 + " μg/m3";
  valueElements.nh3.innerHTML = "NH3 " + airQualityData.list[0].components.nh3 + " μg/m3";

  valueElements.windDirection.innerHTML = hRWindDirection;
  document.querySelector(
    `#${id} img.picture`
  ).src = `./img/weather-${weatherData.weather[0].main}.png`;
}

document.getElementById("searchInput").addEventListener("input", () => {
  clearTimeout(inputDelayTimer);
  inputDelayTimer = setTimeout(() => {
    const query = document.getElementById("searchInput").value;
    if (query == "") {
      return;
    }
    handleSearch(query);
    localStorage.setItem("city", query);
  }, 1000);
});

document.getElementById("searchButton").addEventListener("click", () => {
  const query = document.getElementById("searchInput").value;
  if (query == "") {
    return;
  }
  handleSearch(query);
  localStorage.setItem("city", query);
});

document.addEventListener("DOMContentLoaded", () => {
  const valueFromStorage = localStorage.getItem("city");

  if (valueFromStorage) {
    document.getElementById("searchInput").value = valueFromStorage;
  }
});

// Thunderstorm
// Drizzle
// Rain
// Snow
// Clear
// Clouds

/*
co Сoncentration of CO (Carbon monoxide), μg/m3
no Сoncentration of NO (Nitrogen monoxide), μg/m3
no2 Сoncentration of NO2 (Nitrogen dioxide), μg/m3
o3 Сoncentration of O3 (Ozone), μg/m3
so2 Сoncentration of SO2 (Sulphur dioxide), μg/m3
pm2_5 Сoncentration of PM2.5 (Fine particles matter), μg/m3
pm10 Сoncentration of PM10 (Coarse particulate matter), μg/m3
nh3 Сoncentration of NH3 (Ammonia), μg/m3
*/