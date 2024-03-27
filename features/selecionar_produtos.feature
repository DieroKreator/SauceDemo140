Feature: Selecionar Produto

    Scenario: Selecionar produto "Sauce Labs Backpack"
        Given que acesso o site Sauce Demo
        When preencho os campos de login com usuario standard_user e senha secret_sauce
        Then sou direcionado para página Home

    Scenario: Login com a senha invalida
        Given que entro o site Sauce Demo
        When preencho os campos de login com usuario standard_user e senha laranja
        Then exibe a mensagem de erro no login

    Scenario Outline: Login Negativo
        Given que entro o site Sauce Demo
        When preencho os campos de login com usuario <usuario> e senha <senha>
        Then exibe a <mensagem> de erro no login

        Examples:
        | id | usuario       | senha        | mensagem                                                                  |
        | 01 | standard_user | laranja      | Epic sadface: Username and password do not match any user in this service |
        | 02 | standard_user |              | Epic sadface: Password is required |
        | 03 |               | secret_sauce | Epic sadface: Username is required |
        | 04 | juca          | secret_sauce | Epic sadface: Username and password do not match any user in this service |
        | 05 | juca          | laranja      | Epic sadface: Username and password do not match any user in this service |
        | 06 | juca          |              | Epic sadface: Password is required |
        | 07 |               |              | Epic sadface: Username is required |
        | 08 |               | laranja      | Epic sadface: Username is required |

    Scenario Outline: Login Negativo com IF
        Given que entro o site Sauce Demo
        When digito os campos de login com usuario <usuario> e senha <senha> com IF
        Then exibe a <mensagem> de erro no login

        Examples:
        | id | usuario       | senha        | mensagem                                                                  |
        | 01 | standard_user | laranja      | Epic sadface: Username and password do not match any user in this service |
        | 02 | standard_user | <branco>     | Epic sadface: Password is required |
        | 03 | <branco>      | secret_sauce | Epic sadface: Username is required |
        | 04 | juca          | secret_sauce | Epic sadface: Username and password do not match any user in this service |
        | 05 | juca          | laranja      | Epic sadface: Username and password do not match any user in this service |
        | 06 | juca          | <branco>     | Epic sadface: Password is required |
        | 07 | <branco>      | <branco>     | Epic sadface: Username is required |
        | 08 | <branco>      | laranja      | Epic sadface: Username is required |

    Scenario: Validar o produto no carrinho
        Given que acesso o site Sauce Demo
        And preencho os campos de login com usuario standard_user e senha secret_sauce
        And adiciono um produto ao carrinho
        When clico no icone do carrinho
        Then o produto Sauce Labs Backpack está no carrinho