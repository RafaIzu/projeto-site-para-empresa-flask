const app = document.getElementById('raiz')



const caixa = document.createElement('div')

caixa.setAttribute('class', 'caixa')

app.appendChild(caixa)




for(var i = 0; i < 10; i++){
    var c = document.createElement('div');
    c.setAttribute('class','artigos')
    caixa.appendChild(c)

    var t = document.createElement('h3')
    t.textContent = 'Titulo ' + (i+1)

    c.appendChild(t)

    var p = document.createElement('p')
    p.textContent = 'The orphan Sheeta inherited a mysterious crystal that links her to the mythical sky-kingdom of Laputa.'
    c.appendChild(p)
}

console.log(typeof(document))


