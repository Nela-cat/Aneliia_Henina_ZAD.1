# Zadanie 1 (2. (max. +50%) część dodatkowa) – Aneliia Henina  
Grupa: IO 6.4  
Data: 06.05.2025  

---

##  Cel

Przygotowanie kontenera zgodnego z OCI dla aplikacji pogodowej, zbudowanego na platformy:
- `linux/amd64`
- `linux/arm64`

oraz z użyciem cache przy budowie (eksporter `registry`, backend `inline`).

---

##  Użyte polecenia i działania

## 1. Utworzenie buildera

```bash
docker buildx create --use --name multiarch-builder
docker buildx inspect multiarch-builder --bootstrap


2. Budowa i publikacja obrazu
docker buildx build --platform linux/amd64,linux/arm64 --push --tag nelacot/zad_1_dod:multiarch --cache-to=type=registry,ref=nelacot/zad_1:buildcache,mode=max --cache-from=type=registry,ref=nelacot/zad_1:buildcache .

3. Sprawdzenie manifestu
docker buildx imagetools inspect nelacot/zad_1_dod:multiarch

Wynik:

✅ linux/amd64

✅ linux/arm64

✅ dane cache zapisane








PS C:\6-sem\oblaka\zad1\zadanie1_dod> docker buildx build --platform linux/amd64,linux/arm64 --push --tag nelacot/zad_1_dod:multiarch --cache-to=type=registry,ref=nelacot/zad_1:buildcache,mode=max --cache-from=type=registry,ref=nelacot/zad_1:buildcache .
[+] Building 158.9s (29/29) FINISHED                                                                         docker-container:multiarch-builder
 => [internal] load build definition from Dockerfile                                                                                       0.0s
 => => transferring dockerfile: 1.16kB                                                                                                     0.0s 
 => [linux/amd64 internal] load metadata for docker.io/library/python:3.10-slim                                                            1.3s 
 => [linux/arm64 internal] load metadata for docker.io/library/python:3.10-slim                                                            0.6s 
 => [internal] load .dockerignore                                                                                                          0.0s
 => => transferring context: 109B                                                                                                          0.0s 
 => ERROR importing cache manifest from nelacot/zad_1:buildcache                                                                           0.3s
 => [internal] load build context                                                                                                          0.0s 
 => => transferring context: 657B                                                                                                          0.0s 
 => [linux/amd64 builder 1/5] FROM docker.io/library/python:3.10-slim@sha256:57038683f4a259e17fcff1ccef7ba30b1065f4b3317dabb5bd7c82640a5e  0.0s 
 => => resolve docker.io/library/python:3.10-slim@sha256:57038683f4a259e17fcff1ccef7ba30b1065f4b3317dabb5bd7c82640a5ed64f                  0.0s 
 => [linux/arm64 builder 1/5] FROM docker.io/library/python:3.10-slim@sha256:57038683f4a259e17fcff1ccef7ba30b1065f4b3317dabb5bd7c82640a5e  0.0s 
 => => resolve docker.io/library/python:3.10-slim@sha256:57038683f4a259e17fcff1ccef7ba30b1065f4b3317dabb5bd7c82640a5ed64f                  0.0s
 => CACHED [linux/amd64 builder 2/5] WORKDIR /app                                                                                          0.0s 
 => CACHED [linux/amd64 stage-1 3/6] RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*                          0.0s 
 => CACHED [linux/amd64 builder 3/5] COPY requirements.txt .                                                                               0.0s
 => CACHED [linux/amd64 builder 4/5] RUN pip install --no-cache-dir -r requirements.txt                                                    0.0s 
 => CACHED [linux/amd64 builder 5/5] RUN rm requirements.txt                                                                               0.0s 
 => CACHED [linux/amd64 stage-1 4/6] COPY --from=builder /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages  0.0s 
 => CACHED [linux/amd64 stage-1 5/6] COPY --from=builder /usr/local/bin/ /usr/local/bin/                                                   0.0s 
 => CACHED [linux/amd64 stage-1 6/6] COPY . /app                                                                                           0.0s 
 => CACHED [linux/arm64 builder 2/5] WORKDIR /app                                                                                          0.0s 
 => CACHED [linux/arm64 stage-1 3/6] RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*                          0.0s 
 => CACHED [linux/arm64 builder 3/5] COPY requirements.txt .                                                                               0.0s 
 => CACHED [linux/arm64 builder 4/5] RUN pip install --no-cache-dir -r requirements.txt                                                    0.0s 
 => CACHED [linux/arm64 builder 5/5] RUN rm requirements.txt                                                                               0.0s 
 => CACHED [linux/arm64 stage-1 4/6] COPY --from=builder /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages  0.0s 
 => CACHED [linux/arm64 stage-1 5/6] COPY --from=builder /usr/local/bin/ /usr/local/bin/                                                   0.0s 
 => CACHED [linux/arm64 stage-1 6/6] COPY . /app                                                                                           0.0s 
 => exporting to image                                                                                                                     7.9s 
 => => exporting layers                                                                                                                    0.0s 
 => => exporting manifest sha256:94fc6653690a0a87ec90a99d334236bf38fb28512302b2cce617d04de8467054                                          0.0s 
 => => exporting config sha256:0ed6a38658d34af18a32811b0647cb68e0367f7a2f57bc6b047e1643b769f6a0                                            0.0s 
 => => exporting attestation manifest sha256:8257ade7fba51e0609fd4123875a2e8380ac2d27891fc8e0d37bc5f7bc4deefe                              0.0s 
 => => exporting manifest sha256:a62d8003d7e2d7b00b92ab18d908a9cdea737c63f0bb4a5c7ce70a5550bf37c0                                          0.0s 
 => => exporting config sha256:e6b6299b4504bae624904bd69fcffd9cd02a545718c686076730ca5a1ede7787                                            0.0s 
 => => exporting attestation manifest sha256:4d0d0271730877b85b2d5248c97b6883db1df9bb1907af58ebc6f4103961e17e                              0.0s 
 => => exporting manifest list sha256:e98e5f0ff8f77928d8d83cbea2a8055387fd4a5ee76e1bdbefe8a025e0340dad                                     0.0s 
 => => pushing layers                                                                                                                      3.7s 
 => => pushing manifest for docker.io/nelacot/zad_1_dod:multiarch@sha256:e98e5f0ff8f77928d8d83cbea2a8055387fd4a5ee76e1bdbefe8a025e0340dad  4.1s 
 => [auth] nelacot/zad_1_dod:pull,push token for registry-1.docker.io                                                                      0.0s 
 => [auth] nelacot/zad_1:pull nelacot/zad_1_dod:pull,push token for registry-1.docker.io                                                   0.0s 
 => exporting cache to registry                                                                                                          149.4s 
 => => preparing build cache for export                                                                                                  149.3s 
 => => writing layer sha256:0c8923faddf038a9a3665939c2eea1962aabeeeb007672abd2da6aafcae553d3                                               0.7s 
 => => writing layer sha256:10c5b0bc4dc015ca2734ba941fd64b1013e14bc71b06685fcea5c98dfc772f47                                               0.2s 
 => => writing layer sha256:17814f6ada5d45976ff771376b0ef675a6deea8108cbe47ff0777af598dd8980                                               0.0s 
 => => writing layer sha256:1faf0c2a3490925dfca5184e9815b490c88ee899e175133d3ba07dbc98fe727a                                               0.3s 
 => => writing layer sha256:254e724d77862dc53abbd3bf0e27f9d2f64293909cdd3d0aad6a8fe5a6680659                                               0.6s 
 => => writing layer sha256:4e4d935c4383aa4611cf443010db329c4e4080cb94fa8864c734e4c73109aa19                                               0.8s 
 => => writing layer sha256:501be45329d77435987a90b22e080ea5b202618497f0318af849d9b0bdce44d3                                               0.3s 
 => => writing layer sha256:765ef9c81879b3bfc7185726a38c8b3531b80fc48d6e54d8725a6cabf02c60e1                                               0.3s 
 => => writing layer sha256:7775e85041ae9f0217adad6bd3430df2efe24bc1a0e214d12d4b6089d2458967                                               0.0s 
 => => writing layer sha256:79d166b8e33676489c2f09ee10f0b516ffce03e7aa143ffad3e1104915551121                                               0.5s 
 => => writing layer sha256:92e5f9e5de64a1369423a10d83393bf1a3533dd76c039b32cb0251bffd7ae33d                                               0.3s 
 => => writing layer sha256:943331d8a9a9863299c02e5de6cce58602a5bc3dc564315aa886fe706376f27f                                               0.3s 
 => => writing layer sha256:94f7c93d805cb17ff2bac6197775259af333fd872857a5877e25a6ac22d1f134                                               0.3s 
 => => writing layer sha256:b93be3de8eab3acfd838312cb8cd7edc392b907728a944cc77c39c42ea213bc9                                               0.5s 
 => => writing layer sha256:c9d5a2775b474d02365420e61287559e697b93c87fe3e31df499d270c87227e7                                               0.6s 
 => => writing layer sha256:d15668d6a1de27ac749c4d14e5aa7769b29e8853056f3f17e0678fa13aae1812                                               0.3s 
 => => writing layer sha256:d8651daaa9ee30d413b7eacc7eea6a10afe597f1954aabef4a3581e421c50034                                               0.3s 
 => => writing layer sha256:df007eea74a31e334ec983fe01bc025b73676e29573b2429960f3b0a9869c81f                                               0.3s 
 => => writing layer sha256:e23d4dcfb49323a8cb863fcce985ed1e6eb9747b226358739c1cf2f0027cbbfb                                               0.5s 
 => => writing layer sha256:f5d9e468965706043efe3f59cee3e12ccfd6987410bbc77355c6370babdf2452                                               0.5s 
 => => writing layer sha256:f872075b5a52648fc545a0218954096af54c226ec75d5b8c20047b39ae794e6d                                             135.6s 
 => => writing layer sha256:fb8fd3aff4ebc0639ef4af49e4fc0feab08781cf264df78f96adc80e4920c9d1                                               0.4s 
 => => writing config sha256:08d76b01e6354d1b4a3f770b800b8c991076258a2a6dba183397e67fc3f7268a                                              1.3s 
 => => writing cache manifest sha256:a8530fb635b617128300d0385f1b8c82d918f6e9364175e29cfbaecd7d47a19d                                      3.1s 
 => [auth] nelacot/zad_1:pull,push token for registry-1.docker.io                                                                          0.0s 
------
 > importing cache manifest from nelacot/zad_1:buildcache:
------

View build details: docker-desktop://dashboard/build/multiarch-builder/multiarch-builder0/7d2h69etmaoeabya489ug43zk
PS C:\6-sem\oblaka\zad1\zadanie1_dod> 
PS C:\6-sem\oblaka\zad1\zadanie1_dod> ^C
PS C:\6-sem\oblaka\zad1\zadanie1_dod> docker buildx imagetools inspect nelacot/zad_1_dod:multiarch
Name:      docker.io/nelacot/zad_1_dod:multiarch
MediaType: application/vnd.oci.image.index.v1+json
Digest:    sha256:e98e5f0ff8f77928d8d83cbea2a8055387fd4a5ee76e1bdbefe8a025e0340dad

Manifests:
  Name:        docker.io/nelacot/zad_1_dod:multiarch@sha256:94fc6653690a0a87ec90a99d334236bf38fb28512302b2cce617d04de8467054
  MediaType:   application/vnd.oci.image.manifest.v1+json
  Platform:    linux/amd64

  Name:        docker.io/nelacot/zad_1_dod:multiarch@sha256:a62d8003d7e2d7b00b92ab18d908a9cdea737c63f0bb4a5c7ce70a5550bf37c0
  MediaType:   application/vnd.oci.image.manifest.v1+json
  Platform:    linux/arm64

  Name:        docker.io/nelacot/zad_1_dod:multiarch@sha256:8257ade7fba51e0609fd4123875a2e8380ac2d27891fc8e0d37bc5f7bc4deefe
  MediaType:   application/vnd.oci.image.manifest.v1+json
  Platform:    unknown/unknown
  Annotations:
    vnd.docker.reference.digest: sha256:94fc6653690a0a87ec90a99d334236bf38fb28512302b2cce617d04de8467054
    vnd.docker.reference.type:   attestation-manifest

  Name:        docker.io/nelacot/zad_1_dod:multiarch@sha256:4d0d0271730877b85b2d5248c97b6883db1df9bb1907af58ebc6f4103961e17e
  MediaType:   application/vnd.oci.image.manifest.v1+json
  Platform:    unknown/unknown
  Annotations:
    vnd.docker.reference.digest: sha256:a62d8003d7e2d7b00b92ab18d908a9cdea737c63f0bb4a5c7ce70a5550bf37c0
    vnd.docker.reference.type:   attestation-manifest
