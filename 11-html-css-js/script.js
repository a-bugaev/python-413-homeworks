const apiAnswer = {
  coord: { lon: 37.6156, lat: 55.7522 },
  weather: [{ id: 804, main: "Clouds", description: "пасмурно", icon: "04n" }],
  base: "stations",
  main: {
    temp: 8.12,
    feels_like: 6.25,
    temp_min: 7.24,
    temp_max: 8.52,
    pressure: 1025,
    humidity: 80,
    sea_level: 1025,
    grnd_level: 1005,
  },
  visibility: 10000,
  wind: { speed: 3.01, deg: 247, gust: 7.69 },
  clouds: { all: 100 },
  dt: 1729952527,
  sys: {
    type: 2,
    id: 2094500,
    country: "RU",
    sunrise: 1729916600,
    sunset: 1729951403,
  },
  timezone: 10800,
  id: 524901,
  name: "Москва",
  cod: 200,
};

const geocodeMapsCoApiKey = "67206f61b830e500180237pxnff455c";
const geocodeMapsCoApiUrl = "https://geocode.maps.co/reverse";
// "?lat=latitude&lon=longitude&api_key=api_key"
const getAdress = async () => {
  const response = await fetch(
    `${geocodeMapsCoApiUrl}?lat=${apiAnswer.coord.lat}&lon=${apiAnswer.coord.lon}&api_key=${geocodeMapsCoApiKey}`
  );
  const data = await response.json();
  if (data) {
    const adress = data.display_name;
    return adress
  } else {
    console.warning("Ошибка при получении данных о местоположении");
    return ''
  }
};

const markup = `
<div class="row" id="">
  <div class="col-12">
    <div class="card my-3">
      <div class="row">
        <div class="col-4">
          <img class="card-img-top picture" alt="weather picture">
        </div>
        <div class="col-8">
          <div class="card-body">
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
`

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
  "windDirection"
]

function addWeatherCard(weatherData) {

  const id = `id_${Date.now()}`;

  document.getElementById('weatherContainer').innerHTML += markup.replace(`id=""`, `id="${id}"`);

  let valueElements = {};

  fields.forEach(field => {
    let el = document.createElement('p');
    el.id = `${id}_${field}`;
    el.className = 'card-text';
    document.querySelector(`#${id} .card-body`).append(el);
    valueElements[field] = el;
  });
  
  getAdress().then(data => valueElements.location.innerHTML = data);

  valueElements.date.innerHTML = '<i class="bi bi-calendar"></i>&nbsp;&nbsp;' + 
    new Date(weatherData.dt * 1000).toLocaleDateString();

  valueElements.sunrise.innerHTML = '<i class="bi bi-sunrise"></i>&nbsp;&nbsp;' + 
    new Date(weatherData.sys.sunrise * 1000).toLocaleTimeString();

  valueElements.sunset.innerHTML = '<i class="bi bi-sunset"></i>&nbsp;&nbsp;' + 
    new Date(weatherData.sys.sunset * 1000).toLocaleTimeString();

  valueElements.timeZone.innerHTML = '<i class="bi bi-clock"></i>&nbsp;&nbsp;UTC&nbsp;' + 
    (weatherData.timezone > 0 ? "+" : "-") + (weatherData.timezone / 3600);

  valueElements.tempMax.innerHTML = 'maximum ' + 
    (weatherData.main.temp_max > 0 ? "+" : "-") + Math.round(weatherData.main.temp_max) + " °C";

  valueElements.tempItself.innerHTML = 'current ' +
    (weatherData.main.temp > 0 ? "+" : "-") + Math.round(weatherData.main.temp) + " °C";

  valueElements.feelsLike.innerHTML = "( feels like " +
    (weatherData.main.feels_like > 0 ? "+" : "-") + Math.round(weatherData.main.feels_like) + " °C)";

  valueElements.tempMin.innerHTML = "minimum " +
    (weatherData.main.temp_min > 0 ? "+" : "-") + Math.round(weatherData.main.temp_min) + " °C";

  valueElements.humidity.innerHTML = '<i class="bi bi-droplet"></i> ' + weatherData.main.humidity + '%';

  valueElements.pressure.innerHTML = Math.round((weatherData.main.pressure * 100) / 133.3) + ' мм.рт.ст.';

  valueElements.windSpeed.innerHTML = '<i class="bi bi-wind"></i> ' + weatherData.wind.speed + ' м/с';

  let hRWindDirection = '';
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

  valueElements.windDirection.innerHTML = hRWindDirection;
  document.querySelector(`#${id} img.picture`).src = `./img/weather-${weatherData.weather[0].main}.png`;
}


document.getElementById('showWeatherButton').addEventListener('click', () => {
  addWeatherCard(apiAnswer)
});