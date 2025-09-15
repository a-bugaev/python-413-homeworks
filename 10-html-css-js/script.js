proverbs = [
  "Ум хорошо, а два лучше.",
  "Ум — горячая штука.",
  "Ум всё голова.",
  "Умом Россию не понять.",
  "Ум бережет, а глупость губит.",
  "Ум в голову приходит.",
  "Ум от ума не горит.",
  "Умом нагружен, а волосы развеваются.",
  "Умом обдумал, а ногами пошел.",
  "Ум — сокровище, не пропадет без него и копье на ветру.",
  "Ум — грех, а бес — мера.",
  "Ум есть богатство.",
  "Ум роднит народы.",
  "Ум краток, да забот — бездна.",
  "Ум не камень, взял и положил.",
  "Ум не велит, а наставляет.",
  "Ум с мерой, а глупость без меры.",
  "Ум — сокол, глаз его — телескоп.",
  "Ум — не конская морда, не разобьешь.",
  "Ум — семь пядей во лбу.",
  "Ум — не барсук, в нору не залезет.",
  "Ум в голове, а не на ветру.",
  "Ум греет душу, а глупость терпение.",
  "Ум служит человеку, а глупость — хозяином.",
  "Ум мил, да безумству хозяин.",
  "Ум в труде, да наслаждение в праздности.",
  "Ум глаза исправляет.",
  "Ум человека не обманешь.",
  "Ум на подобии огня — без сна не останешься.",
  "Ум к уму приходит.",
  "Ум с пользой тратит время.",
  "Ум желание творит.",
  "Ум общего дела дело.",
  "Ум — друг, а воля — враг.",
  "Ум — бесценное сокровище.",
  "Ум тонок, да разум невелик.",
  "Ум — враг бедности.",
  "Ум — теремок, да не на прокол.",
  "Ум силен, да не камень.",
  "Ум рассудит, что сердце не посоветует.",
  "Ум — подкова, а топор — ось.",
  "Ум легче камня, да весомей золота.",
  "Ум не вешать на гроздья.",
  "Ум — не мешок, на плечи не вешай.",
  "Ум — лучшая победа.",
  "Ум — в суде велик, а в деле своем мал.",
  "Ум голове краса.",
  "Ум — сокровище, а глупость — нищета.",
  "Ум человека — огонь, а глаза — масло.",
  "Ум — путь, а дорога — конец.",
  "Ум стоит денег.",
  "Ум от смеха бьет в ладоши.",
  "Ум — коза, к барскому плечу привыкает.",
  "Ум — лезвие, а лень — ржавчина.",
  "Ум на вершине — мир в руках."
]

variants = [
  'кот',
  'шеф',
  'мозг',
  'лес',
  'фолк',
  'код',
  'рот',
  'мёд',
  'лук',
  'лес',
  'год',
  'час',
  'друг',
  'жена',
  'муж',
  'айфон',
  'работа'
]

let proverbsCopy = [...proverbs];
let variantsCopy = [...variants];

generateAllPossibleProverbs = (srcProverbs, srcWords) => {
  let result = [];

  srcProverbs.forEach(proverb => {
    srcWords.forEach(word => {
      result.push(proverb.replace('Ум', word))
    })
  })
  
  return result
}

var allPossibleProverbs = generateAllPossibleProverbs(proverbsCopy, variantsCopy);
var allPossibleProverbsCopy = [...allPossibleProverbs];

selectMultipleProverbs = (qty, proverbs) => {
  let result = [];
  for (let i = 0; i < qty; i++) {
    let randomIndexOfProverb =
      Math.abs(
        Math.round(
          Math.random() * (proverbs.length - 1)
        )
      )
    let randomProverb = proverbs[randomIndexOfProverb];
    result.push(randomProverb);
    proverbs.splice(randomIndexOfProverb, 1);
  }
  return result;
}

displayMultipleProverbs = (proverbs) => {
  let proverbsUl = document.getElementById('proverbsUl');
  proverbs.forEach(proverb => {
    let proverbLi = document.createElement('li');
    if (!(proverbsUl.children.length+1 > 935)) {
      proverbLi.innerText = proverbsUl.children.length+1 + ') ' + proverb;
      proverbsUl.appendChild(proverbLi);
    }
  })
}

document.getElementById('resetButton').addEventListener('click', () => {
  proverbsCopy = [...proverbs];
  variantsCopy = [...variants];
  allPossibleProverbsCopy = [...allPossibleProverbs];
  document.getElementById('proverbsUl').innerHTML = '';
});

document.getElementById('generateButton').addEventListener('click', () => {
  let qty = document.getElementById('qtyInput').value;
  displayMultipleProverbs(
    selectMultipleProverbs(qty, allPossibleProverbsCopy)
  );
});