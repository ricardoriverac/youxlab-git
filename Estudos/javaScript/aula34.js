const curso=[...document.querySelectorAll(".curso")]
cursosC1.map((el)=>{
    el.addEventListener("click", (evt)=>{
        const el = evt.target
        el.classList.add("destaque")
        console.log(el.innerHTML + "foi clicado")
    })
})

//el.addEventListener("click", (evt)=>{
    //const el=evt.target
    //el.classList.add("destaque")})