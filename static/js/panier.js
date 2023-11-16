var produitBtns = document.getElementsByClassName('update-panier');

for (var i = 0; i < produitBtns.length; i++){

    produitBtns[i].addEventListener('click', function(){

        var produitId = this.dataset.produit;

        var action = this.dataset.action;

        if (user === "AnonymousUser"){
            console.log(produitId, action);
        }else{
            updateUserCommande(produitId, action);
        }
    })

}


function updateUserCommande(produitId, action){

    var url = '/update_article/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({"produit_id": produitId, "action": action})
    })

    .then((response) => {
        return response.json();
    })

    .then((data) => {
        console.log('data', data);
        location.reload();
    })
}