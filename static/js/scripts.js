function chart(chartId, label, values){
  const labels = label;
  const data = values;
     // Criando o gráfico de barras
     const ctx = document.getElementById(chartId).getContext('2d');
     const serviceChart = new Chart(ctx, {
         type: 'bar',  // Tipo de gráfico (barra)
         data: {
             labels: labels,  // Rótulos dos serviços
             datasets: [{
                 label: 'Quantidade de Serviços',
                 data: data,  // Quantidade de ocorrências de cada serviço
                 backgroundColor: 'rgba(54, 162, 235, 0.2)',
                 borderColor: 'rgba(54, 162, 235, 1)',
                 borderWidth: 1
             }]
   },
   options: {
     scales: {
       y: {
         beginAtZero: true
       }
     }
   }
 });
}

// static/js/scripts.js
function setupDynamicHourSelection(dateFieldId = "id_date", hourFieldId = "id_hour") {
  const dateField = document.getElementById(dateFieldId);
  const hourField = document.getElementById(hourFieldId);

  if (!dateField || !hourField) return;

  dateField.addEventListener("change", function () {
      const selectedDate = this.value;
      if (!selectedDate) return;

      fetch(`/get-available-hours/?date=${selectedDate}`)
          .then(response => response.json())
          .then(data => {
              hourField.innerHTML = '';
              if (data.hours.length === 0) {
                  const option = document.createElement('option');
                  option.text = "Nenhum horário disponível";
                  option.value = "";
                  hourField.add(option);
              } else {
                  data.hours.forEach(hour => {
                      const option = document.createElement('option');
                      option.text = hour;
                      option.value = hour;
                      hourField.add(option);
                  });
              }
          })
          .catch(error => {
              console.error("Erro ao buscar horários disponíveis:", error);
          });
  });
}

console.log("scripts.js carregado");  // ← Adicione isso para teste
