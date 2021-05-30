const context = JSON.parse(document.getElementById('context').textContent);


// Gender data chart
new Chart(document.getElementById("gender-chart"), {
    type: 'doughnut',
    data: {
      labels: Object.keys(context.genders),
      datasets: [
        {
          label: "Gender",
          backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f"],
          data: Object.values(context.genders)
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: 'Genders from uploaded user data'
      }
    }
});


new Chart(document.getElementById("firstname-chart"), {
    type: 'polarArea',
    data: {
      labels: ["A-M", "N-Z"],
      datasets: [
        {
          label: "First Names",
          backgroundColor: ["#3e95cd", "#8e5ea2"],
          data: Object.values(context.names.first)
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: 'First names A-M versus N-Z from uploaded user data'
      }
    }
});


new Chart(document.getElementById("lastname-chart"), {
    type: 'polarArea',
    data: {
      labels: ["A-M", "N-Z"],
      datasets: [
        {
          label: "Last Names",
          backgroundColor: ["#3e95cd", "#8e5ea2"],
          data: Object.values(context.names.last)
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: 'Last names A-M versus N-Z from uploaded user data'
      }
    }
});

console.log(context.locations)

// let values = []
// for (const state in context.locations) {
//   values.push(context.locations[state].percentageAllUsers)
// }
//

let values = []
for(const state in context.locations)
{
    values.push(context.locations[state].percentageAllUsers)
}


new Chart(document.getElementById("locations-chart"), {
    type: 'radar',
    data: {
      labels: Object.keys(context.locations),
      datasets: [
        {
          label: "States",
          backgroundColor: ["#3e95cd", "#8e5ea2"],
          data: values
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: 'People living in top 10 states'
      }
    }
});