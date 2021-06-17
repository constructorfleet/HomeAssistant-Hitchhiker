Home-Assistant Hitchhiker Implementation
=========

Home-Assistant implementation of a Hitchhiker for the Guide.

Requirements
------------

TODO

Role Variables
--------------

### Overridable Variables
`hitchhiker_architecuture` - The system architecture  
`hitchhiker_name` - The name of the Hitchhiker  
`homeassistant_components` - A list of components to be installed  
`hitchhiker_admin_user` - Specification for the admin user  
`hitchhiker_users` - A list of users to automatically register with the application

### Valid Architectures 
`aarch64` - 64-bit ARM Architecture   
`armhf` - 32-bit ARM Hard-Float Architecture
`armv7` - 31-bit/64-bit ARM Architecture  
`amd64` - 64-bit AMD Architecture
`i386` - 32-bit Intel Architecture

### Home-Assistant Component Specification
* Core Components  
    `src` - core  
    `name` - Name of the component to be installed  
    `verson` - Home-Assistant version to retrieve component from
* HACS component  
    `src` - hacs  
    `name` - Name of the component to be installed
    `repo` - The HACS repository that contains the component  
    `version` - The repository version to retrieve component from  

### User Specification
`username` - Login username that does not contain [- .!^$*]  
`password` - Login password that, it cannot be empty  
`name` - Optional display name for the user, will default to the username

Dependencies
------------

TODO

Example Playbook
----------------

TODO

License
-------

MIT

Author Information
------------------

Teagan Glenn (@Teagan42)
