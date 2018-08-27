$(document).ready(function () {
        $('.input_text').keydown(function () {

            var text = $('.input_text').val()
            if (text == '') {

                $('.modal-header').removeClass('active')
                $('.panel-heading').removeClass('active')

            } else {

                                        // $('.modal-header').addClass('active')
            }


        });






    })

