import cmd
import time

class interface(cmd.Cmd):
    prompt = "co-ficcient>"
    intro = "\nbem vindo ao co-ficcient,digite ajuda para uma lista de comandos.\n"

    comandos_ajuda = {
        "iniciar": "Inicia o montador de equação do segundo grau",
        "criador": "Mostra o nome do criador do script",
        "sair": "Encerra o programa",
        "ajuda": "Mostra essa tabela"
    }

    def do_criador(self, arg):
        print("script criado por ezequiel( @ezequielz1456 )")

    def do_sair(self, arg):
        while True:
            sair_d = input("Tem certeza que quer sair do co-ficcient? (s/n): ").strip().lower()
        
            if sair_d == "s":
                print("Saindo...")
                return True
        
            elif sair_d == "n":
                print("Cancelado.")
                break
        
            else:
                print("Escolha entre 's' ou 'n'!")

    def do_iniciar(self, arg):
        while True:
            try:
                ca = float(input("Digite o valor do coeficiente A: "))
        
                if ca != 0:
                    cb = float(input("Digite o valor do coeficiente B: "))
                    cc = float(input("Digite o valor do coeficiente C: "))
                    print("calculando...")
                    time.sleep(1)
                    print(f"{ca:.0f}x²")
                    time.sleep(1)
                    print(f"{cb:.0f}x")
                    time.sleep(1)
                    print(f"{cc:.0f}")
                    time.sleep(1)
                    if cb==0:
                        print(f"{ca:.0f}x²")
                        if ca == 1:
                            p1 = "x²"
                        else:
                            p1 = f"{ca:.0f}x²"                            
                    elif cb>0:
                        print(f"{ca:.0f}x²+{cb:.0f}x")
                        if ca == 1:
                            p1 = f"x²+{cb:.0f}x"
                        else:
                            p1 = f"{ca:.0f}x²+{cb:.0f}x"
                    else:
                        print(f"{ca:.0f}x²{cb:.0f}x")
                        if ca == 1:
                            p1 = f"x²{cb:.0f}x"
                        else:
                           p1 = f"{ca:.0f}x²{cb:.0f}x"
                    time.sleep(1)
                    if cc>0:
                        print(f"{p1}+{cc:.0f}")
                    else:
                        print(f"{p1}{cc:.0f}")
                    time.sleep(1)
                    print("\n")
                    if cc == 0:
                        print(f"resposta final é: {p1} = 0")
                        print("\n")
                        break
                    elif cc>0:
                        print(f"resposta final é: {p1}+{cc:.0f} = 0")
                        print("\n")
                        break
                    else:
                        print(f"resposta final é: {p1}{cc:.0f} = 0")
                        print("\n")
                        break

                else:
                    print("O número não pode ser 0. Tente novamente.")
            except ValueError:
                 print("Entrada inválida. Digite um número.")
    
    def do_ajuda(self, arg):
        print("\nTabela de comandos:\n")
        print(f"{'Comando':<10} | {'Descrição'}")
        print("-" * 40)
        for cmd, desc in self.comandos_ajuda.items():
            print(f"{cmd:<10} | {desc}")
        print()

if __name__ == '__main__':
    interface().cmdloop()