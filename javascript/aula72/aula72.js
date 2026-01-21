const teclasNum = [...document.querySelectorAll(".num")]
const teclasOp = [...document.querySelectorAll(".op")]
const teclasRes = document.querySelector(".res")
const display = document.querySelector(".display")

teclasNum.forEach((el)=>{
    el.addEventListener("click", (evt)=>{
        display.innerHTML += evt.target
    })
})