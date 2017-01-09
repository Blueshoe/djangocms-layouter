(function() {
    var $ = CMS.$;
    var csrftoken = $('[name="csrfmiddlewaretoken"]').val();
    var toggleGridButton = document.getElementsByClassName('js-layouterMenu')[0];
    $(toggleGridButton).click(function(e) {
        e.preventDefault();
       var r = new XMLHttpRequest();
        $.ajax({
            method: 'POST',
            url: toggleGridURL,
            data: {toggle: true, csrfmiddlewaretoken: csrftoken},
            success: function(data) {
                if (data['show_grid']) {
                    $('.layouterRow--inner').addClass('show-grid');
                    $(toggleGridButton).addClass('cms-btn-active').blur();
                }
                else {
                    $('.layouterRow--inner').removeClass('show-grid');
                    $(toggleGridButton).removeClass('cms-btn-active').blur();
                }

            },
            error: function() {
                alert('Something went wrong toggling the grid.')
            }

        });
    });
})();