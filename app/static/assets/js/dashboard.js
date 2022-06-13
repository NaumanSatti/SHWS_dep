$(function(){
    // $('area').click(function(){
    //     alert($(this).attr('alt'));
    // })
    // console.log('sanity check')

    $('area').each(function(){
       
        var alt_value = $(this).attr("alt");
        var alt_value = '/visualization/' + alt_value;
        $(this).attr('href',alt_value)

        
    })
})