document.getElementById("submitButtoncito").addEventListener("click", function(event) {
    event.preventDefault(); // Evitar el envío del formulario por defecto
    
    // Obtener el valor seleccionado del elemento <select>
    let locationValue = document.getElementById("locationSelect").value;
     let locationName = document.getElementById("locationSelect").options[document.getElementById("locationSelect").selectedIndex].text;
    let bdns_like = document.getElementById("searching").value;
    
    // Declarar la variable formAction
    let formAction;
    
    // Agregar el valor seleccionado como parámetro a la URL de acción del formulario
    if (locationValue !== "" && bdns_like === "") {
        formAction = "/subsidy/subsidloc/" + encodeURIComponent(locationValue) + "/" + encodeURIComponent(locationName);
    } else if (bdns_like !== "" && locationValue === "") {
        formAction = "/subsidy/bdns_like/" + encodeURIComponent(bdns_like);
    } else if (locationValue !== "" && bdns_like !== "") {
        formAction = "/subsidy/bdns_location/" + encodeURIComponent(bdns_like) + "/" + encodeURIComponent(locationValue) + "/" + encodeURIComponent(locationName);
    }

    // Establecer la nueva URL de acción para el formulario
    document.getElementById("searchFormulario").setAttribute("action", formAction);
    
    // Enviar el formulario
    document.getElementById("searchFormulario").submit();
});

/* search by title like name*/

document.getElementById("title_search").addEventListener("submit", (e) => {
    e.preventDefault();
  
    const title = document.getElementById('searchTitle').value;
  
    if (title !== "") {
        const formAction = "/subsidy/title_like/" + encodeURIComponent(title);
        document.getElementById("title_search").setAttribute("action", formAction);
        document.getElementById("title_search").submit();
    }
});


