{ pkgs ? import <unstable> {} }:

let
  shellname = "python";

  mach-nix = import (
  builtins.fetchGit {
      url = "https://github.com/DavHau/mach-nix/";
      ref = "2.0.0";
    }
  );

  mods = mach-nix.mkPython {
    python = pkgs.python39;
    requirements = ''
      python-vlc
    '';
  };

  myPython = with pkgs; [
    poetry
    python39Packages.sly
    python39Packages.rich
  ];
in
  pkgs.stdenv.mkDerivation {
    name = shellname;
    buildInputs = [
      myPython
      mods
    ];
    shellHook = ''
      export NIX_SHELL_NAME='${shellname}'
      alias p='python3'
      alias gg='docker run --rm --name dockagator \
        -v "$(pwd)":/project \
        -v "dockagator":/root/.local/share \
        gatoreducator/dockagator'
    '';
  }
