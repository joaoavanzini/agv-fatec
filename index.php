
<html>
    <head>
        <!-- CSS only -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
        <!-- JS, Popper.js, and jQuery -->
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7JlabelAgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.4/js/bootstrap.min.js"></script>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.4/css/bootstrap.min.css" rel="stylesheet"/>
        
        <script>
        function onlyOne(checkbox) {
            var checkboxes = document.getElementsByName('check')
            checkboxes.forEach((item) => {
                if (item !== checkbox) item.checked = false
            })
        }
        </script>
        <script>
            $(document).ready(function () {
                $('input[id="cat1"]').on('change', function (e) {
                    if (e.target.checked) {
                        $('#myModal1').modal();
                    }
                });
            })
            $(document).ready(function () {
                $('input[id="cat2"]').on('change', function (e) {
                    if (e.target.checked) {
                        $('#myModal2').modal();
                    }
                });
            })
            $(document).ready(function () {
                $('input[id="cat3"]').on('change', function (e) {
                    if (e.target.checked) {
                        $('#myModal3').modal();
                    }
                });
            })
            $(document).ready(function () {
                $('input[id="cat4"]').on('change', function (e) {
                    if (e.target.checked) {
                        $('#myModal4').modal();
                    }
                });
            })
        </script>

    </head>
    <body>
        <br>
            <div class="container">
              <h1 class="d-flex justify-content-center">Escolha uma opção...</h1>
              <div class="shadow-lg p-4 mb-4 bg-white">
                    <div class="checkbox d-flex justify-content-center">
                    <label><input type="checkbox" id="cat1" value="1" name="check" onclick="onlyOne(this)"> Segue linha</label>
                    </div>
                    <div class="checkbox d-flex justify-content-center">
                    <label><input type="checkbox" id="cat2" value="2" name="check" onclick="onlyOne(this)"> Segue linha e desvia dos objetos</label>
                    </div>
                    <div class="checkbox d-flex justify-content-center">
                    <label><input type="checkbox" id="cat3" value="3" name="check" onclick="onlyOne(this)"> Controle WEB</label>
                    </div>      
                    <div class="checkbox d-flex justify-content-center">
                    <label><input type="checkbox" id="cat4" value="4" name="check" onclick="onlyOne(this)"> Controle Joystick</label>
                    </div>
                </div>
            </div>
            <div class="modal fade" id="myModal1" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                        </div>
                        <div class="modal-body">
                            Confirmar Segue linha?
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-default" data-dismiss="modal">Fechar</button>
                            <form action="inserir.php" method="post">
                                <input type="hidden" id="op1" name="op" value=1>
                                <input type="submit" class="btn btn-primary" value="Confirmar">
                            </form>                            
                        </div>
                    </div>
                </div>
            </div>
            <div class="modal fade" id="myModal2" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                        </div>
                        <div class="modal-body">
                            Confirmar Segue linha e desvia dos objetos?
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-default" data-dismiss="modal">Fechar</button>
                            <form action="inserir.php" method="post">
                                <input type="hidden" id="op2" name="op" value=2>
                                <input type="submit" class="btn btn-primary" value="Confirmar">
                            </form>                            
                        </div>
                    </div>
                </div>
            </div>
            <div class="modal fade" id="myModal3" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                        </div>
                        <div class="modal-body">
                            Confirmar Controle WEB?
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-default" data-dismiss="modal">Fechar</button>
                            <form action="inserir.php" method="post">
                                <input type="hidden" id="op3" name="op" value=3>
                                <input type="submit" class="btn btn-primary" value="Confirmar">
                            </form>                            
                        </div>
                    </div>
                </div>
            </div>
            <div class="modal fade" id="myModal4" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                        </div>
                        <div class="modal-body">
                            Confirmar Controle Joystick?
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-default" data-dismiss="modal">Fechar</button>
                            <form action="inserir.php" method="post">
                                <input type="hidden" id="op4" name="op" value=4>
                                <input type="submit" class="btn btn-primary" value="Confirmar">
                            </form>                            
                        </div>
                    </div>
                </div>
            </div>
    </body>

</html>
