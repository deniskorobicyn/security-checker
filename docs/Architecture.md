### Top level parts

- security checker
- storage
- dashboard
- VCS integration

### Development parts
- database integration
- self-hosted
- config
- tests


### Security checker

#### Ideal
- can check any type of language
- easily extendable

#### MVP 0
- check python code
- check repo only once (no PR or anything like that)
- no diff
- find all vulnerabilities using pip-audit or OSV database
- show list of vulnerabilities on the dashboard
- allow to add more projects

### MVP 1
- TBD

##### problems accured
 - safety is paid tool eventually
 - all tools are based on top of NVD or smth like that

#### additional ideas
- use of https://osv.dev/list
- direct usage of databases for vulnerailities
- main feature of the project is dashboards and overview of all vulnerabilities
- extract tool for osv access for poetry into cli


#### dashboard ideas
 - project overview of all vulnerabilities found
 -
