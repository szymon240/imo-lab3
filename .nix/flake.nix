{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }: 
  let 
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
    fetchurl = pkgs.fetchurl;
    packageOverrides = pkgs.callPackage ./python-packages.nix { inherit pkgs fetchurl; };
    pythonCustom = pkgs.python3.override { inherit packageOverrides; };
  in 
  {
    devShells.${system}.default = pkgs.mkShell {
      packages = with pkgs; [
        python3

        python3Packages.numpy_1
        python3Packages.matplotlib
        (pythonCustom.withPackages(p: [ p.tsplib95 ]))
      ];
    };
  };
}
