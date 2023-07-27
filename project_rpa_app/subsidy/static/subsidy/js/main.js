
/*Click desde la tabla muestra un modal con un detalle*/
document.addEventListener('DOMContentLoaded', function() {



  /*Code para modal al hacer click  en una rows*/
  var rows = document.querySelectorAll('.row-detail');
  rows.forEach(function(row) {
    row.addEventListener('click', function() {
      var bdns = row.getAttribute('data-bdns');
        console.log("Cliqueado en "+ bdns);
      fetch('/subsidy/bdns/?bdns__like=' + bdns)
      .then(function(response) { return response.json(); })
      .then(function(response) {

        var subsidy = response.subsidy[0];
        console.log(subsidy);

        let supportTypesHtml = '';

        if (subsidy.support_type && subsidy.support_type.length > 0) {
          subsidy.support_type.forEach((supportType, index) => {
            supportTypesHtml += `<li><b>Support Type ${index + 1} Code:</b> ${supportType.code}</li>`;
            supportTypesHtml += `<li><b>Support Type ${index + 1} Name:</b> ${supportType.name}</li>`;
          });
        } else {
          supportTypesHtml = '';
        }

          // Ahora llena el modal con estos detalles
       var details = `<ul>
       <li><b>BDNS:</b> ${subsidy.bdns}</li>
       <li><b>Title:</b> ${subsidy.title}</li>
       <li><b>Link:</b> <a href="${subsidy.link}">${subsidy.link}</a></li>
       <li><b>Convening Authority ID:</b> ${subsidy.convening_authority.id}</li>
       <li><b>Convening Authority Name:</b> ${subsidy.convening_authority.name}</li>
       ${subsidy.online_office ? `<li><b>Online Office:</b> <a href="${subsidy.online_office}">${subsidy.online_office}</a></li>` : ''} 
       <li><b>Registration_date:</b> ${subsidy.registration_date}</li>
       ${supportTypesHtml}
       <li><b>Type Code:</b> ${subsidy.type.code}</li>
       <li><b>Type Name:</b> ${subsidy.type.name}</li>
       <li><b>Budget:</b> ${subsidy.budget}€</li>
       <li><b>Beneficiary Code:</b> ${subsidy.beneficiary_type[0].code}</li>
       <li><b>Beneficiary Name:</b> ${subsidy.beneficiary_type[0].name}</li>
       <li><b>Beneficiary Economic Sector:</b> ${subsidy.beneficiary_economic_sector}</li>
       <li><b>Location Code:</b> ${subsidy.location.code}</li>
       <li><b>Location Name:</b> ${subsidy.location.name}</li>
       <li><b>Purpose Code:</b> ${subsidy.purpose.code}</li>
       <li><b>Purpose Name:</b> ${subsidy.purpose.name}</li>
       <li><b>Start Date:</b> ${subsidy.start_date}</li>
       <li><b>End Date:</b> ${subsidy.end_date}</li>
       <li><b>Regulatory Base:</b> ${subsidy.regulatory_bases}</li>
       <li><b>Regulatory Base Address:</b> <a href="${subsidy.regulatory_bases_address}">${subsidy.regulatory_bases_address}</a></li>

       ${subsidy.official_journal ? `<li><b>Official Journal:</b> ${subsidy.official_journal}</li>` : ''}
       ${subsidy.sa_number_ref ? `<li><b>Number Ref:</b> ${subsidy.sa_number_ref}</li>` : '' } 
       ${subsidy.objetives ? `<li><b>Objetives:</b> ${subsidy.objetives}</li>` : ''}
       ${subsidy.rules_eu ? `<li><b>Rules EU:</b> ${subsidy.rules_eu}</li>` : ''}
       ${subsidy.product_sector ? `<li><b>Product Sector:</b> ${subsidy.product_sector}</li>` : ''}
       </ul>

       `;

       document.querySelector('#subsidyModal .modal-body').innerHTML = details;

          // Finalmente, muestra el modal
       var modal = new bootstrap.Modal(document.getElementById('subsidyModal'));
       modal.show();
     });
    });
  });
});


/*
Busqueda por input sear by bdsn
*/

document.getElementById('searchForm').addEventListener('submit', function(event) {
  // Prevent default form submission
  event.preventDefault();

  let bdns = document.getElementById('searchInput').value;
  fetch('/subsidy/bdns/?bdns__like=' + bdns)
  .then(function(response) { return response.json(); })
  .then(function(response) {
    let subsidy = response.subsidy[0];
    console.log(subsidy);

    let supportTypesHtml = '';

    if (subsidy.support_type && subsidy.support_type.length > 0) {
      subsidy.support_type.forEach((supportType, index) => {
        supportTypesHtml += `<li><b>Support Type ${index + 1} Code:</b> ${supportType.code}</li>`;
        supportTypesHtml += `<li><b>Support Type ${index + 1} Name:</b> ${supportType.name}</li>`;
      });
    } else {
      supportTypesHtml = '';
    }

      // Ahora llena el modal con estos detalles
    let details = `<ul>
    <li><b>BDNS:</b> ${subsidy.bdns}</li>
    <li><b>Title:</b> ${subsidy.title}</li>
    <li><b>Link:</b> <a href="${subsidy.link}">${subsidy.link}</a></li>
    <li><b>Convening Authority ID:</b> ${subsidy.convening_authority.id}</li>
    <li><b>Convening Authority Name:</b> ${subsidy.convening_authority.name}</li>
    ${subsidy.online_office ? `<li><b>Online Office:</b> <a href="${subsidy.online_office}">${subsidy.online_office}</a></li>` : ''}
    <li><b>Registration_date:</b> ${subsidy.registration_date}</li>
    ${supportTypesHtml}
    <li><b>Type Code:</b> ${subsidy.type.code}</li>
    <li><b>Type Name:</b> ${subsidy.type.name}</li>
    <li><b>Budget:</b> ${subsidy.budget}€</li>
    <li><b>Beneficiary Code:</b> ${subsidy.beneficiary_type[0].code}</li>
    <li><b>Beneficiary Name:</b> ${subsidy.beneficiary_type[0].name}</li>
    <li><b>Beneficiary Economic Sector:</b> ${subsidy.beneficiary_economic_sector}</li>
    <li><b>Location Code:</b> ${subsidy.location.code}</li>
    <li><b>Location Name:</b> ${subsidy.location.name}</li>
    <li><b>Purpose Code:</b> ${subsidy.purpose.code}</li>
    <li><b>Purpose Name:</b> ${subsidy.purpose.name}</li>
    <li><b>Start Date:</b> ${subsidy.start_date}</li>
    <li><b>End Date:</b> ${subsidy.end_date}</li>
    <li><b>Regulatory Base:</b> ${subsidy.regulatory_bases}</li>
    <li><b>Regulatory Base Address:</b> <a href="${subsidy.regulatory_bases_address}">${subsidy.regulatory_bases_address}</a></li>

    ${subsidy.official_journal ? `<li><b>Official Journal:</b> ${subsidy.official_journal}</li>` : ''}
    ${subsidy.sa_number_ref ? `<li><b>Number Ref:</b> ${subsidy.sa_number_ref}</li>` : '' } 
    ${subsidy.objetives ? `<li><b>Objetives:</b> ${subsidy.objetives}</li>` : ''}
    ${subsidy.rules_eu ? `<li><b>Rules EU:</b> ${subsidy.rules_eu}</li>` : ''}
    ${subsidy.product_sector ? `<li><b>Product Sector:</b> ${subsidy.product_sector}</li>` : ''}
    </ul>`;

    document.querySelector('#subsidyModal .modal-body').innerHTML = details;

      // Finalmente, muestra el modal
    var modal = new bootstrap.Modal(document.getElementById('subsidyModal'));
    modal.show();
    document.getElementById('searchInput').value = '';
  });
});

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
