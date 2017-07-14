/**
 * Created by baran.topal on 2017-07-14.
 */

$(function () {
    $('.btnAdd').click(function () {
        var id = $('#id').val();
        var name = $('#name').val();
        var age = $('#age').val();
        var type = $('#type').val();
        $.ajax({
            url: '/addEmployee',
            data: $('form').serialize(),
            type: 'POST',
            success: function (response) {
                console.log(response);
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});

$(function () {
    $('.btnGet').click(function () {
        $.ajax({
            type: "GET",
            url: "/getEmployeeList",
            contentType: "application/json; charset=utf-8",

            success: function (data) {
                // console.log("data:" + data);

                var jsonData = $.parseJSON(data);
                var trHTML = '';
                // requires improvement outer loop shall not be necessary
                $.each(JSON.parse(jsonData), function (i, item) {

                    // not intuitive enough
                    var el = item.Personnels.Employee;

                    $.each(el, function (key, value) {
                        trHTML += '<tr><td>' + value.Name + '</td><td>' + value.Id + '</td><td>' + value.Age + '</td><td>' + value.type + '</td></tr>';
                    });

                });
                $('#result').append(trHTML);

            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});