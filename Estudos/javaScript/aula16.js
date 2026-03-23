let num = [10,20,30,40,50]

const objs = document.getElementsByTagName("div")

//for(let i = 0; i<num.length;i++){
  //  console.log(num[i])
//}

for(o of objs){
    console.log(o.innerHTML="Curso")
}
