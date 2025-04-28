Feature: Login de intu
    Scenario: Credenciales incorrectas intu
        Given el usuario se encuentra en la página login de intu
        When el usuario ingresa credenciales erroneas
        Then aparece un mensaje de error