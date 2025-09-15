/*
попытка сделать вменяемый ввод номера
*/

const form = document.querySelector(".custom-form")
const phoneInput = document.querySelector(".phone-input")
if (phoneInput) {
    const normalBg = phoneInput.style.backgroundColor;
}

var mask = "+7 (___) ___ __ __"

var numberArr = []

var phoneNumberLengthLimit = 12

function highlightWarning(inputTag) {
    /*
    kinda flash on each wrong input from keyboard
    */
    setTimeout(() => {
        inputTag.style.backgroundColor = "rgba(211, 84, 0, 0.25)";
        setTimeout(() => {
            inputTag.style.backgroundColor = normalBg;
        }, 150);
    });
}

function isDigit(str) {
    return /^\d+$/.test(str);
}

function takeOffMask(input = null) {
    if (input) {
        return input.replaceAll(/[^\d\+]/g, "")
    } else {
        return phoneInput.value.replaceAll(/[^\d\+]/g, "")
    }
}

function isExtra(str) {
    return takeOffMask(phoneInput.value) + str.length <= phoneNumberLengthLimit
}

function addToMask(str) {
    let i = 0
    while (i <= str.length - 1) {
        mask = mask.replace(/_/, str[i])
        i++
    }
}

function replaceAtIndex(str, idx, newChar) {
    return str.split('').map((char, i) => i === idx ? newChar : char).join('')
}

function reverseStr(str) {
    return str.split('').reverse().join('')
}

function backspaceFromMask() {
    let reversed = reverseStr(mask)
    let reversed_cutted = reversed.replace(/..$/, "")
    let digitIdx = reversed_cutted.search(/\d/)
    if (typeof digitIdx == "number" && digitIdx >= 0) {
        let backspaced = replaceAtIndex(reversed_cutted, digitIdx, "_")
        let straight = reverseStr(backspaced)
        mask = "+7" + straight
    }
}

if (phoneInput) {
    phoneInput.addEventListener("input", (e) => {

        if (e.data == null) {
            e.preventDefault()
            backspaceFromMask()
        }

        if (isDigit(e.data) && !isExtra(e.data)) {
            addToMask(e.data)
        }
        if (!isDigit(e.data) && e.data !== null) {
            e.preventDefault()
            highlightWarning(e.target)
        }
        e.target.value = mask
    })
}

function getPhoneValue() {
    return takeOffMask()
}

if (form) {
    form.addEventListener("submit", () => {
        phoneInput.value = getPhoneValue()
    })
}
/*
данные о мастерах и услугах воткнуты в json формате в window в соседнем скрипте
(см. core/templates/forms/create_order.html )
*/

const masters_services_arr = window.masters_services_arr;

/*
на каждый выбор мастера в селекте нужно изменить содержимое селекта услуг
валидация на уровне джанго формы тоже выполняется (core/forms.py)
*/

const masterSelect = document.querySelector("select#id_master")
const servicesSelect = document.querySelector("select#id_services")

function adjustOptions(masterDOM, servicesDOM) {
    servicesDOM.innerHTML = ""
    const selectedMasterId = masterDOM.value
    let servicesWeNeed = []
    masters_services_arr.forEach(master_obj => {
        if (master_obj.master_id == selectedMasterId) {
            servicesWeNeed = [...master_obj.master_services]
        }
    })
    servicesWeNeed.forEach(service_obj => {
        optionDOM = document.createElement("option")
        optionDOM.value = service_obj.service_id
        optionDOM.textContent = service_obj.service_name
        servicesDOM.appendChild(optionDOM)
    })
}
if (masterSelect && servicesSelect && masters_services_arr) {
    window.addEventListener("load", () => {
        adjustOptions(masterSelect, servicesSelect)
    })
    masterSelect.addEventListener("change", (e) => {
        adjustOptions(e.target, servicesSelect)
    })
    masterSelect.addEventListener("focus", (e) => {
        adjustOptions(e.target, servicesSelect)
    })
}
/*
поведение для ввода рейтинга
*/

const ratingWrapper = document.querySelector(".rating-input-wrapper")
if (ratingWrapper) {
    const ratingInput = ratingWrapper.querySelector("input")
    const ratingStars = [...ratingWrapper.querySelectorAll("i")]
}

function setRating(value) {
    ratingInput.value = value
    ratingStars.forEach(star => {
        if (/\d/.exec(star.id) <= value) {
            star.classList.add("light")
        } else {
            star.classList.remove("light")
        }
    })
}

if (ratingWrapper) {
    ratingStars.forEach(star => {
        star.addEventListener("click", (e) => {
            setRating(/\d/.exec(e.target.id))
        })
        star.addEventListener("click", (e) => {
            setRating(/\d/.exec(e.target.id))
        })
    })
    ratingInput.addEventListener("change", (e) => {
        setRating(e.target.value)
    })
    ratingInput.addEventListener("focus", (e) => {
        setRating(e.target.value)
    })
}