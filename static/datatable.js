$(document).ready(function() {
    mysql_return = mysql
    console.log(mysql_return)
    $('#example').DataTable( {
        data: mysql_return,
        columns: [
            { title: "Employee Number" },
            { title: "Birth Date" },
            { title: "First Name" },
            { title: "Last Name" },
            { title: "Gender" },
            { title: "Hire Date" }
        ]
    } );
} );