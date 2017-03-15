$(function () {
    //make menus drop automatically
    $('ul.nav li.dropdown').hover(
        function() {
        $('.dropdown-menu', this).fadeIn("fast");
    }, function () {
        $('.dropdown-menu', this).fadeOut("fast");
    });
});