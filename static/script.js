const title = document.getElementById('title');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const calenderBloc = document.getElementById('calenderBloc');

var currDate = new Date();

function main(){
    buildCalender(currDate);

    prevBtn.addEventListener('click', function(){changeMonth(-1)});
    nextBtn.addEventListener('click', function(){changeMonth(1)});
}

function buildCalender(date){
    const currMonth = date.getMonth();
    const currYear = date.getFullYear();

    const firstDay = new Date(currYear, currMonth, 0).getDay();
    const lastDate = new Date(currYear, currMonth + 1, 0).getDate();

    var months = ['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December'];

    title.textContent = `${months[currMonth]} ${currYear}`
    calenderBloc.innerHTML = '';

    var dateRow = document.createElement('tr');
    for (let i = 0; i < firstDay; i++) {
        const emptyCell = document.createElement('td');
        dateRow.appendChild(emptyCell);
    }

    for (let day = 1; day <= lastDate; day++) {
        if (dateRow.children.length === 7) {
            calenderBloc.appendChild(dateRow);
            dateRow = document.createElement('tr');
        }
        const dateCell = document.createElement('td');
        dateCell.textContent = day;
        dateRow.appendChild(dateCell);
    }

    if (dateRow.children.length > 0) {
        calenderBloc.appendChild(dateRow);
    }
}

function changeMonth(value){
    currDate.setMonth(currDate.getMonth() + value);
    buildCalender(currDate);
}

document.addEventListener('DOMContentLoaded', main());