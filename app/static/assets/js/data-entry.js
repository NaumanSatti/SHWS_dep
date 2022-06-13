
//   window.onload = function() {
//     if (window.jQuery) {  
//         // jQuery is loaded  
//         alert("Yeah!");
//     } else {
//         // jQuery is not loaded
//         alert("Doesn't Work");
//     }
// }
i = 1
j = 1
$(function(){
    
    // at the first hide all accordion except first one
    hide_accordion(i)
    $("[data-datefield]").hide();
    $("[type=submit]").hide();


    // set date auto matically to date field
    document.getElementById('datePicker').valueAsDate = new Date();

    // first hide all the buttons
    $("button[type=next]").prop('disabled', true);

     // for auto total function
     calculate_total_household_with_source_of_drinking_water();

    //  check if input type number has negative or not
    $('input[type=number]').each(function(){
        var element = $(this);
        element.keyup(function(){
            if (element.val() < 0){
                element.val(0)
                alert('Value cannot be entered in negative')
            }
        })
    })
});


// to calulate auto total in household water source and sewerage 
function calculate_total_household_with_source_of_drinking_water(){
    $('input[aria-labelledby=sourceofdrinkingwater]').keyup(function(){
        var total_value = 0;
        $('input[aria-labelledby=sourceofdrinkingwater]').map(function(){
            var element = $(this);
            total_value = total_value + parseFloat(element.val())
        })
        $('input[name=totalhouseholdwithdrinkingwatersource]').val(total_value);

        toogle_nextbutton('data-accordionlevel='+i);
    });
    
    $('input[aria-labelledby=seweragesystem]').keyup(function(){
            var total_value = 0;
            $('input[aria-labelledby=seweragesystem]').map(function(){
                var ele = $(this);
                total_value = total_value +parseFloat(ele.val());
            });
            $('input[data-seweragetotal]').val(total_value)
        
            toogle_nextbutton('data-accordionlevel='+i);
    });
    
}

// check value entered in input field to toggle next button
function check_value_entered_or_not(){
    toogle_nextbutton('data-accordionlevel='+i);

    // this above is because toogle navigation only works after key
    $("[data-accordionlevel="+i+"] :input").keyup(function(){
        toogle_nextbutton('data-accordionlevel='+i);
      });

     
      
}


// function to hide and show according to level
function hide_accordion(i){
    $('.accordion-item').hide();
    $('.accordion-item[data-accordionlevel='+i+'], .accordion-item[data-accordionsublevel='+i+']').show();
   
    // check if form fields are entered or not 
    check_value_entered_or_not();

    // when we reach to last next then we have to show submit form button to
    if(i == 10){
        // $('input[name=datesubmitted]').show();
        $("[data-datefield]").show();
        $("button[type=submit]").show();
    }
}

// to show next accordion and collapse previous accordion
function show_accordion(j){
    console.log('sanity checck')
    var preaccor = j - 1
    $('.accordion-item[data-accordionlevel='+preaccor+'] > div:first').removeClass("show");
    $('.accordion-item[data-accordionlevel='+j+']').show();

    check_value_entered_or_not();

    // when we reach to last next then we have to show submit form button to
    if(i == 10){
        // $('input[name=datesubmitted]').show();
        $("[data-datefield]").show();
        $("button[type=submit]").show();
    }
}

// function to show next button after input fileds are inputted
function toogle_nextbutton(collapselevel){
    // to check if all the input fields are entered or not
        var isValid = true;
        $("["+collapselevel+"]").find('input').each(function() {
            var element = $(this);
            if (element.val() == '') {
                isValid = false;
            }
        });

        //  show next button only after all input fields are 
        if(isValid){
           $('['+collapselevel+'] :button[type=next]').prop('disabled', false);
        }else{
            $('['+collapselevel+'] :button[type=next]').prop('disabled', true); 
        }
}


// function to increment the value of i when next button is clicked
$('button[type=next]').click(function(e){
    e.preventDefault();
    j++;
    i++;
    show_accordion(j);
    // hide_accordion(i)


});