function myFunction() {
    champ = document.getElementById('price_sugar');
    champ.value=document.getElementById('qty_sugar').value;
}

document.addEventListener("DOMContentLoaded", function() {
    const qtyElements = document.querySelectorAll(".qty"); // Sélectionne tous les éléments avec la classe "qty"

    qtyElements.forEach(function(element) {
        if (element.id!='qty_sugar'){
        element.addEventListener("change", myFunction); // Ajoute l'événement "change"
        element.addEventListener("keyup", myFunction);
        }  // Ajoute l'événement "keyup"
    });
});


document.addEventListener("DOMContentLoaded", function() {
    const json_date_of_birth = JSON.parse(document.getElementById('json_date_of_birth').textContent); //va chercher dans le html la variable nommée json_date_of_birth
    document.getElementById('date_birth').value=json_date_of_birth;

    const json_weight2 = JSON.parse(document.getElementById('json_weight').textContent);
    document.getElementById('weight').value=json_weight2;

    const json_height = JSON.parse(document.getElementById('json_height').textContent);
    document.getElementById('height').value=json_height;

    const json_children = JSON.parse(document.getElementById('json_children').textContent);
    document.getElementById('children').value=json_children;

    const json_sex = JSON.parse(document.getElementById('json_sex').textContent);
    document.getElementById('test').value=json_sex;
    if (json_sex=='male'){
        document.getElementById('sex_option_1').selected=true;

    }
    else{
        document.getElementById('sex_option_2').selected=true;

    }

    const json_smoker = JSON.parse(document.getElementById('json_smoker').textContent);
    if (json_smoker=='yes'){
        document.getElementById('smoker_option_1').selected=true;

    }
    else{
        document.getElementById('smoker_option_2').selected=true;

    }

    const json_region = JSON.parse(document.getElementById('json_region').textContent);
    switch (json_region){
        case 1:
        document.getElementById('region_option_1').selected=true;
        case 2:
        document.getElementById('region_option_2').selected=true;
        case 3:
        document.getElementById('region_option_3').selected=true;
        case 4:
        document.getElementById('region_option_4').selected=true;
        
        default:
            console.log("Bad region value")
    }





});

function print_user() {
    const user_name = JSON.parse(document.getElementById('username').textContent);
    document.getElementsByName('test')[0].value=user_name
}