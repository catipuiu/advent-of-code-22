# un arbore, un nod = file -> nume, type(director sau regular file), size(fisiee normale, cat e dat, pt foldere se calculeaza pe parcurs), parent(referinta la alt file care e parent ca sa poti naviga in sus la parinte)
# toate fisierele normale au dimensiuni dar folderele n au, etapa in care trebuie sa parcurgi arborele si sa calculezi dimensiunea folderelor -> dfs (suma unui folder e dimensiunea tutror copiilor lui)-> reapelare recursiva
