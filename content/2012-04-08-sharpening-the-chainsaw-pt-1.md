Title: Sharpening the chainsaw pt. 1
Date: 2012-04-08 23:15
Tags: git, unix, linux, environments, zsh
Slug: sharpening-the-chainsaw-pt-1
Category: Linux

I recently got into Ruby development with some help from [Jesse Dearing](http://jessedearing.com) and [James Gifford](https://plus.google.com/103797989648432285071/posts) and I found my shell environment to be quite a bit lacking. It wasn't Exactly vanilla, but It needed some help.

I also learned quite a bit about some of the trending habits among Vim developers along the way. Upgrading my entire vim setup to use [Pathogen](https://github.com/tpope/vim-pathogen) instead of the mess that was my .vim directory. Essentially, pathogen offers an easy way to add plugins to your Vim setup without all the messy manual config work.

>Manage your 'runtimepath' with ease. In practical terms, pathogen.vim makes it super easy to install plugins and runtime files in their own private directories.

### Pimping vim with Pathogen

Lets take a look at this a bit closer...
<!-- More -->

As some of you know, I use git almost religiously. And keeping my [dotfiles](https://github.com/chuckbutler/dotfiles) in a repository has made system upgrades among other things a real breeze. But more on this later. _note_ dont let the extra steps in setting up your own dotfiles repository sway you from doing so. It saves so much time in the long run - simply set it, and forget it.


To get started using pathogen, you simply clone the pathogen repository into your ~/.vim and move the script into your autoload directory

```
    mv pathogen.vim ~/.vim/autoload
```
Dont forget to add the Pathogen specific bits into your vimrc. (You read the (read)[https://github.com/tpope/vim-pathogen/blob/master/README.markdown]readme file right?)

```
call pathogen#infect()
```

Pure win, at this point. So lets grab a plugin and test drive it.

```
mkdir -p ~/.vim/bundle
cd ~/.vim/bundle
git clone https://github.com/vim-scripts/The-NERD-tree.git
```

This will swipe the latest copy of the nerdtree plugin and keep it isolated in its own directory. Fire up vim and tell it to open the drawer

```
 :NERDTreeToggle
```

You should see something similiar to the following

<img src="/img/posts/vim-drawer.png" alt="NERDTree" />

We've now confirmed that this works.. but wait.. I keep all my dotfiles in a git repository... isn't the NERDTree plugin already IN a git repository? Why would we track files in our own repository that are already published in git? This is exactly what Git Submodules were intended for. So lets start off by cleaning up what we just did, and then re-applying it as a submodule. _*sidenote - if you're not currently keeping your vim configuration/plugins version controlled, you can disregard this step_.

```
rm -rf ~/.vim/bundle/The-Nerd-Tree
cd <The Root of your dotfiles Repo>
git submodule add https://github.com/vim-scripts/The-NERD-tree.git <path/to/your/dot-vim/bundle/NERDTree>

```

You will notice that this adds a new file to your repository. _.gitmodules_ This stores all the information for your submodules - and is important if you ever decide to clone your repository on another machine. More on this a bit later as well.. lets verify that NERDTree cloned itself properly. Fire up vim, and toggle NERDTree again.

```
:NERDTreeToggle
```

If you saw the drawer pop out, everything is working as expected. You can now clone any vim plugin into your bundle directory and without any fuss add / remove them at whill thanks to the awesomeness that is Pathogen + gitsubmodules. So, Lets just say I have two machines, my Desktop and a Laptop. I'd like to keep a consistent environment between the two, and I have all of this setup, lets just pull the updates from our dotfiles repository and verify. Go ahead and issue a git pull on the repository after you've pushed your updates.

### Wat?
You see the directories, but theres __NOTHING IN THEM!__

Don't panic, we have to tell git that we have submodules in this repository, and to initialize them

```
git submodule init
git submodule update
```

After running these two commands you should see git pull the repositories we've added and if you cd into them, all the files will be present and accounted for. Pure win. Lets move on

## Why I switched to ZSH ##

The short answer: its all [Jesse's](http://jessedearing.com) fault. We had a pair programming session over TMUX and i fell in love with the bell's and whistles in his ZSH setup.

<img src="/img/posts/zsh-shell-diagram.png" alt="ZSH Prompt Diagram" />

So enough of that. How can I make the switch to ZSH?


```
sudo apt-get install zsh
```

#### If you're using a dotfiles Repository -- Follow this ####

```
cd <dotfiles repository>
git submodule add https://github.com/robbyrussell/oh-my-zsh.git <path to shell files>
cp <path/to/cloned/oh-my-zsh>/templates/zshrc.zsh-template <path/to/shell files>/dotzshrc
ln -s ~/.oh-my-zsh <path to cloned oh-my-zsh-subdirectory>
ln -s ~/.zshrc <path/to/dotzshrc>
chsh -s /usr/bin/zsh
```

#### If you're not using a dotfiles Repository ####

```
curl -L https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh | sh

```

>You might need to modify your PATH in ~/.zshrc if you’re not able to find some commands after switching to Oh My Zsh.

__*Note* I had to change my exec params in Gnome-Terminal to launch /usr/bin/zsh instead of the system shell. I missed something somewhere, but a set once and forget it.__



Since  [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh) has some extremely good documentation - I'll point you [there](https://github.com/robbyrussell/oh-my-zsh/blob/master/README.textile) for further customization of your new shell.


So in the last 20 minutes or so, we've managed to clean up Vim plugin management, and make it a breeze to port, and swapped over to a shell with some nice bells and whistles. I'll follow up with more on maintaining your dotfiles repository in part 2, and where to go from there.
