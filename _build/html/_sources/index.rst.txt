.. Forca_ASCII documentation master file, created by
   sphinx-quickstart on Wed Apr 14 18:57:25 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Seja bem-vindo a documentação de Forca_ASCII!
=============================================

Desenvolvedores: Ana Carolina Erthal Fernandes, Eduardo Adame Salles, Murilo Calegari de Souza, Tiago Barradas Figueiredo, Rodrigo Gomes Hutz Pintucci e Vinícius Hedler


Repositório: https://github.com/adamesalles/forcaASCII


Instruções de jogo:

1. Tenha Python instalado na sua máquina. Nós utilizamos a versão 3.8.8 para desenvolver.
2. Certifique-se que os arquivos ``main.py``, ``modulo_grafico.py`` e ``palavras_temas.txt`` no mesmo diretório.
3. Execute o arquivo ``main.py``. No Linux (nossa plataforma de desenvolvimento), ``python3 main.py``. No Windows, ``py .\main.py``.
4. Se divirta!

Obs: se quiser adicionar palavras, não há limitação quando à açentuação ou hifenização/espaçamento em nosso software. No entanto, coloque em cada linha uma palavra e sua respectiva dica no formato "palavra;dica".

Também é importante ressaltar que as funções que limpam o terminal foram definidas e criadas pelo módulo gráfico, que não é de nossa autoria. Neste caso, nós percebemos que os comandos por eles utilizados para limpar o terminal não têm total compatibilidade com o Windows.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Sumário
==================

* :ref:`genindex`
* :ref:`modindex`

Módulos
=======

.. automodule:: main
   :members:


Source Code
===========

Main
--------

.. literalinclude:: main.py
  :language: python


