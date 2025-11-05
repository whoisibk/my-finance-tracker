const add_trans = document.getElementById('circle-transac');
const close_form = document.getElementById('form-close');

const main_popup = document.getElementById('add-transac');
const overlay_popup = document.getElementById('overlay-popup');
const save_form = document.getElementById('form-save');
const form_popup = document.getElementById('form-popup');

function openPopup(){
    overlay_popup.classList.add('show');
    main_popup.classList.add('show');
    document.body.style.overflow = 'hidden';
};

function closePopup(){
    overlay_popup.classList.remove('show');
    main_popup.classList.remove('show');
    document.body.style.overflow = '';
};

add_trans.addEventListener('click', ()=> {openPopup()})
close_form.addEventListener('click', ()=>{closePopup()})

save_form.addEventListener('click', async (e)=>{
    e.preventDefault();
    const formData = new FormData(form_popup);
    const response = await fetch('/dashboard', {
        method: 'POST',
        body: formData
    });
    if (response.ok){
        // alert('IT worked')
        overlay_popup.classList.remove('show');
        main_popup.classList.remove('show');
        document.location.reload();
        form.reset();
    }
    else{
        alert('Error saving transaction!');
    }
});

 fetch("/piechart")
        .then(res => res.json())
        .then(data => {
            const ctx = document.getElementById("pie-chart_");

            new Chart(ctx, {
                type: "pie",
                data: {
                    labels: data.labels,
                    datasets: [{
                        data: data.values,
                        backgroundColor: [
                            "#6898c9","#c96d68", "#ccd61aff",
                            "#68c968", "#9966FF", "#d77514ff"
                        ]
                    }]
                },
                options: {
                    responsive: true,
                    radius: '69%',
                    plugins: {
                        legend: {
                            position: "top",
                        },
                        // // title: {
                        // //     display: true,
                        // //     text: ""
                        // },
                        tooltip: {
                            callbacks: {
                                label: ctx => `${ctx.label}: ${ctx.parsed}%`
                            }
                        }
                    }
                }
            });
        });


 fetch("/barchart")
        .then(res => res.json())
        .then(data => {
            const ctx_ = document.getElementById('bar-chart_');

            new Chart(ctx_, {
            type: 'bar',
            data: {
            labels: data.labels,
            datasets: [{
                data: data.values,
                backgroundColor:["#6898c9", "#c96d68"],
                barThickness:85,
                borderWidth: 1
            }]
            },
            options: {
                plugins:{
                legend:{
                    display:false,
                },
                },
                layout:{
                    padding:{
                        top:40,
                    },
                },
            scales: {
                y: {
                    ticks:{
                        autoskip:true,
                        maxTicksLimit:6,
                        precision:0,
                        beginAtZero: true, 
                    },
                    grid:{
                        display: false
                    }
                }
            }
            }
        });
});