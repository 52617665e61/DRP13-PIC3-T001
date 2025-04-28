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


