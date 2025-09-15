
window.addEventListener("load", () => {
    const toastsArr = [...document.querySelectorAll(".toast")]
    toastsArr.forEach(toastDOM => {
        toastObj = window.bootstrap.Toast.getOrCreateInstance(toastDOM)
        toastObj.show()
    })
    console.log("tosts inited")
})
