let rephoto=document.getElementById('rephoto')



function f1(model,color){

    console.log(model,color)
    rephoto.setAttribute('src','/static/js/'+model+' '+color+'.png')
}