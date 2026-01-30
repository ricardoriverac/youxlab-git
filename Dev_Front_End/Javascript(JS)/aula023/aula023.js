function soma(...valores){
    let res=0
    for(let v of valores){
        res+=v
    }
    return res
}

console.log(soma(10,45,23,9))