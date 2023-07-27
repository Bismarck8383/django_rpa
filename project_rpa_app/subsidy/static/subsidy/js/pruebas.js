/*Esta Funcion sirve para el option*/
const get_datos = async () => {
  try {
    const response = await fetch('/subsidy/locations/');
    const data = await response.json();

    //console.log('Datos de locations....');
    //console.log(data);

    let select = document.getElementById('locationSelect');
    select.innerHTML = "";

    // Agregar la opción por defecto "Choose location" sin valor seleccionado
    let defaultOption = document.createElement('option');
    defaultOption.text = "Choose location";
    defaultOption.value = "";
    defaultOption.selected = true; // Establecer como opción seleccionada por defecto
    select.appendChild(defaultOption);

    if (Array.isArray(data)) {
      data.forEach((location) => {
        let option = document.createElement('option');
        option.text = location.name;
        option.value = location.code;
        select.appendChild(option);
      });
    } else {
      console.log('Datos no encontrados');
    }

    select.addEventListener('change', function () {
      let selectedOption = this.options[this.selectedIndex];
      let selectedText = selectedOption.value;
      console.log(selectedText);
    });

  } catch (e) {
    console.log(e);
  }
};

const cargaInicial = async () => {
  await get_datos();
};

window.addEventListener("load", async () => {
  await cargaInicial();
});
