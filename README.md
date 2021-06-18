Home-Assistant Hitchhiker Implementation
=========

Home-Assistant implementation of a Hitchhiker for the Guide.

Requirements
------------

TODO

Role Variables
--------------

### Overridable Hitchhiker Variables
`hitchhiker_architecuture` - The system architecture  
`hitchhiker_name` - The name of the Hitchhiker  
`homeassistant_components` - A list of components to be installed  
`hitchhiker_admin_user` - Specification for the admin user  
`hitchhiker_users` - A list of users to automatically register with the application

#### Valid Architectures 
`aarch64` - 64-bit ARM Architecture   
`armhf` - 32-bit ARM Hard-Float Architecture
`armv7` - 31-bit/64-bit ARM Architecture  
`amd64` - 64-bit AMD Architecture
`i386` - 32-bit Intel Architecture

#### Home-Assistant Component Specification
* Core Components  
    `src` - core  
    `name` - Name of the component to be installed  
    `verson` - Home-Assistant version to retrieve component from
* HACS component  
    `src` - hacs  
    `name` - Name of the component to be installed
    `repo` - The HACS repository that contains the component  
    `version` - The repository version to retrieve component from  

#### User Specification
`username` - Login username that does not contain [- .!^$*]  
`password` - Login password that, it cannot be empty  
`name` - Optional display name for the user, will default to the username

### Home-Assistant Configuration

`homeassistant_home_latitude` - Required decimal-based latitude (-90..90) where the home is located  
`homeassistant_home_longitude` - Required decimal-based longitude (-180..180) where the home is located    
`homeassistant_home_elevation` - Required elevation in meters for the home, must be positive  
`homeassistant_unit_system` - Unit system the instance should use, options: imperial, metric  
`homeassistant_timezone` - Timezone the instance should report time using, i.e. America/Denver  

### Options

#### Authentication (WIP)

To enable and configure the LDAP authentication provider, set the following variable:

```yaml
ldap_auth_provider:
  debug: no
  client: ldapsearch
  timeout_seconds: 3
  ldap_server: "ldap://ldap-server:389"
  name_attribute: cn
  extra_attributes: ""
  user_pattern: "^[a-z|A-Z|0-9|_|-|.]+$"
  user_dn: uid=$(ldap_dn_escape "$username"),ou=people,dc=example,dc=com
```


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
