READ ME

git init
git remote add origin https://github.com/...
--
git add *  <-- <a stage>
git commit -m "message" <al main>
git push origin master


git bash

git status
...origin/main
ls .git/
ls -all <ver todos los archivos del repositorio>

<agregar un nuevo branch> 
    git checkout -b "ticket1" 
<donde estoy>
    git branch 
<listar, donde estoy y archivos no presentes en el repositorio - rojo es oculto>
    git branch -a 
<cambiarse de branch>
    git checkout ... 
<bajar todo lo nuevo del repo, sin integrar al local>
    git fetch 
<bajar código e integrar directamente al branch que uno se encuentra>
    git pull
<crear un branch igual al creado localmente>
    git branch --set-upstream origin <nombre del branch>
<no determinar a donde se debe commitear ? > 
    git pull --set-upstream origin <...>
<resolver/verificar conflictos ?>
    git merge
<verificar todos los cambios realizados en el branch: ordenados del nuevo al +viejo>
    git log -p
<idem pero en una sola linea>
    git log --pretty=oneline
<Integrar commits en uno solo?? - abre un Vim> 
    git rebase -i HEAD-3 




<CREAR> 
    git clone https://github.com/.....
    cd qa-repo-test
    git config user.name "tomasB"
    git config user.email "tb***@***"
    ssh-keygen
    > default location (enter) => C:\Users\User\.ssh
    > empty for no passphrase (enter) => 3 times backspace :D
-- 
    settings > ssh gpg keys > ssh keys / add new	
    title: 
    key: <ssh-rsa pub>

<SETTINGS>
      cat .git/config
      git config --list
    <edit values>
        git config remote.origin.url "git@github.com:...
