$(document).ready(function() {
    $.getJSON('./asset/actor.json', function(items){
        $.each(items, function(i, item){
            $("#chats").append(`<div class="section__text mdl-cell mdl-cell--10-col-desktop mdl-cell--6-col-tablet mdl-cell--3-col-phone"> <div class="datetime">${item[0]}</div> <h5>${item[1]}</h5> ${item[2]} </div>`);
        });
    });

    const chipSetEl = document.querySelector('.mdc-chip-set');
    const chipSet = new mdc.chips.MDCChipSet(chipSetEl);

    $('.mdc-chip').on('click', function(){
        a = $(this).is(".mdc-chip--selected");
        b = $(this).children('div:eq(1)').text();
        c = $(".mdc-chip--selected").length;
        d = $( `h5:contains("${b}")` );
        if(c==0) {
            $(".section__text").hide();
        }
        if(a===true) {
            d.parent().show();
        } else {
            d.parent().hide();
        }

        
    });
});