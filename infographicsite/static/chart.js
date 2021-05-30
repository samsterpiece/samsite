const context = JSON.parse(document.getElementById('context').textContent);


// Example 1
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

//Example 2
new Chart(document.getElementById("firstname-chart"), {
    type: 'polarArea',
    data: {
      labels: ["A-M", "N-Z"],
      datasets: [
        {
          label: "First Names",
          backgroundColor: ["FF00FF", "#8e5ea2"],
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

//Example 3
new Chart(document.getElementById("lastname-chart"), {
    type: 'polarArea',
    data: {
      labels: ["A-M", "N-Z"],
      datasets: [
        {
          label: "Last Names",
          backgroundColor: ["#452984", "#8e5ea2"],
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

//Example 4
let values = []
for(let state in context.locations)
{
    console.log("State: ", state)
    console.log(context.locations[state])
    values.push(context.locations[state].generalUserCount)

}

new Chart(document.getElementById("locations-chart"), {
    type: 'doughnut',
    data: {
      labels: Object.keys(context.locations),
      datasets: [
        {
          label: "States",
          backgroundColor: ["#FF00FF", "#FF0000","#FFA500", "#80b938", "#8d5100",
          "#ebbaf8","#dcb218","#c69df5", "#452984","#85409b",],
          data: values
        }
      ]
    },
    options: {
        plugins: {
        labels:{
        render: 'percentage',
        fontColor: ['white'],
        precision: 2
        }
    },
      title: {
        display: true,
        text: 'People living in top 10 states'
      }
    }
});


//Example 5
values = []
for(let state in context.locations)
{
    console.log("State: ", state)
    console.log(context.locations[state])
    values.push(context.locations[state].femaleUserCount)

}

new Chart(document.getElementById("female-chart"), {
    type: 'doughnut',
    data: {
      labels: Object.keys(context.locations),
      datasets: [
        {
          label: "States",
          backgroundColor: ["#FF00FF", "#FF0000","#FFA500", "#80b938", "#8d5100",
          "#ebbaf8","#dcb218","#c69df5", "#452984","#85409b",],
          data: values
        }
      ]
    },
    options: {
        plugins: {
        labels:{
        render: 'percentage',
        fontColor: ['white'],
        precision: 2
        }
    },
      title: {
        display: true,
        text: 'Percentage of Females living in top 10 states'
      }
    }
});

//Example 6
values = []
for(let state in context.locations)
{
    console.log("State: ", state)
    console.log(context.locations[state])
    values.push(context.locations[state].maleUserCount)

}

new Chart(document.getElementById("male-chart"), {
    type: 'doughnut',
    data: {
      labels: Object.keys(context.locations),
      datasets: [
        {
          label: "States",
          backgroundColor: ["#FF00FF", "#FF0000","#FFA500", "#80b938", "#8d5100",
          "#ebbaf8","#dcb218","#c69df5", "#452984","#85409b",],
          data: values
        }
      ]
    },
    options: {
      plugins: {
        labels: {
        render: 'percentage',
        fontColor: ['white'],
        precision: 2
      }
    },
      title: {
        display: true,
        text: 'Percentage of Males living in top 10 states'
      }
    }
});


//Example 6- Included nonbinary for inclusive purposes
//No data currently shows, however should a JSON file
//Including nonbinary identities is implemented,
//Graph will reflect that
values = []
for(let state in context.locations)
{
    console.log("State: ", state)
    console.log(context.locations[state])
    values.push(context.locations[state].nonbinaryUserCount)

}
new Chart(document.getElementById("nonbinary-chart"), {
    type: 'doughnut',
    data: {
      labels: Object.keys(context.locations),
      datasets: [
        {
          label: "States",
          backgroundColor: ["#FF00FF", "#FF0000","#FFA500", "#80b938", "#8d5100",
          "#ebbaf8","#dcb218","#c69df5", "#452984","#85409b",],
          data: values
        }
      ]
    },
    options: {
      plugins: {
        labels:{
        render: 'percentage',
        fontColor: ['white'],
        precision: 2
      }
    },
      title: {
        display: true,
        text: 'Percentage of Nonbinary living in top 10 states'
      }
    }
});

//Example 7-Age ranges
new Chart(document.getElementById("age-chart"), {
    type: 'doughnut',
    data: {
      labels: Object.keys(context.ages),
      datasets: [
        {
          label: "States",
          backgroundColor: ["#FF00FF", "#FF0000","#FFA500", "#80b938", "#8d5100",
          "#ebbaf8","#dcb218","#c69df5", "#452984","#85409b",],
          data: Object.values(context.ages)
        }
      ]
    },
    options: {
      plugins: {
        labels:{
        render: 'percentage',
        fontColor: ['white'],
        precision: 2
      }
    },
      title: {
        display: true,
        text: 'Percentage Of People In Va'
      }
    }
});



