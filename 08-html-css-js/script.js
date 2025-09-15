// Секретное послание
const secretLetter = [
  ['DFВsjl24sfFFяВАДОd24fssflj234'],
  ['asdfFп234рFFdо24с$#afdFFтasfо'],
  ['оafбasdf%^о^FFжа$#af243ю'],
  ['afпFsfайFтFsfо13н'],
  ['fн13Fа1234де123юsdсsfь'],
  ['чFFтF#Fsfsdf$$о'],
  ['и$##sfF'],
  ['вSFSDам'],
  ['пSFоsfнрSDFаSFвSDF$иFFтsfaсSFя'],
  ['FFэasdfтDFsfоasdfFт'],
  ['FяDSFзFFsыSfкFFf']
];

// Массив с маленькими русскими буквами
const smallRus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
  'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
  'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'];

let messageWeAreDecodingFor = '';

for (let i = 0; i < secretLetter.length; i++) {
  // каждое вхождение исходного массива это массив с единственной строкой, поэтому:
  secretLetter[i] = secretLetter[i][0].split('');
  // теперь имеем 11 массивов с символами

  let wordWeAreDecodingFor = '';

  // используем здесь Array.includes(), а вывод получаем строкой
  for (let j = 0; j < secretLetter[i].length; j++) {
    if (smallRus.includes(secretLetter[i][j])) {
      wordWeAreDecodingFor += secretLetter[i][j]
    }
  }

  // соединяем слова в фразу через пробел
  messageWeAreDecodingFor += wordWeAreDecodingFor + ' ';
}

console.log("Расшифрованное послание: ", messageWeAreDecodingFor);