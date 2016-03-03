Title: Configure nginx using Vagrant and Puppet
Date: 2016-02-11
Tags: vagrant, puppet

Here's a simple exercise, a hello world example for using Vagrant and Puppet together to congifure nginx. I'm going to use an existing Vagrant box from puppetlabs, specifically Ubuntu 12.04 precise. Then use Vagrant to:

1. Specify VM name and URL to fetch the Virtual Machine image
2. Specify port forwarding from guest to host
3. Specify VirtualBox as VM provider
4. Specify a bootstrap.sh script for initial VM configuration
5. Configure puppet and specify a manifest file for configuring nginx
6. Specify a verify.sh script for post-provisioning verification of nginx

Steps 1-3 are self-explanatory and can be found in the [github repo](https://github.com/angelga/puppetlabs_hw/blob/master/Vagrantfile).

### Step 4

Here's where we tell Vagrant to run a shell script so we can do the initial configuration of our VM, install puppet and git, and update the VM. Additionally, we ca perform more specific configuration as per our needs. In my case, I want nginx to serve the content of another github repo, so I git clone the repo, copy the contents into my desired path, and later configure nginx to use this path as the site root.

There are two important consideration we have to make when writing shell scripts for Vagrant. First, they need to be [idempotent](https://en.wikipedia.org/wiki/Idempotence), i.e., they have to be written such that they can be run multiple times without changing the state of the VM (or only change it if needed), and not to execute unnecessary actions. For example, only clone a repo if the repo doesn't exist. Otherwise, try to pull the latest changes (as per our requirements in this example):

```
echo "Clone site repo"
if [ ! -d ~/html ]; then
    git clone https://github.com/puppetlabs/exercise-webpage ~/html
else
    cd ~/html
    git pull
fi
```

Second, always verify your actions and provide meaningful errors when they fail. Also, keeping in mind the concept of idempotency, make sure you don't fail unnecessarily in subsequent script runs. For example, don't assume apt-get install will succeed, specifically check for this:

```
# Check everything is configured correctly
if [ $(command -v puppet) >/dev/null 2>&1 ]; then
    echo "Puppet installed correctly"
else
    echo "Puppet not installed correctly"
    exit 1
fi
```

### Step 5

We need to configure Vagrant to use Puppet with the following lines:

```
config.vm.provision :puppet do |puppet|
    puppet.manifests_path = "puppet/manifests"
    puppet.manifest_file  = "site.pp"
    puppet.module_path = "puppet/modules"
    puppet.options = "--verbose --debug"
end
```

Site.pp is our configuration file. It basically tells puppet which packages to install, files to copy, symlink, etc. It uses a `require` elective to specify prerequisites like have nginx service run only after it's already installed. What I found confusing was copying files to the image. Consider this step:

```
# Add a vhost template
file { 'vagrant-nginx':
    path => '/etc/nginx/sites-available/puppet.technical.assessment.conf',
    ensure => file,
    require => Package['nginx'],
    source => 'puppet:///modules/nginx/puppet.technical.assessment.conf',
}
```

The path *puppet:///modules/nginx/* actually correspond to *modules/nginx/**files*** on the host.

### Step 6

Lastly, I decided to have a verify.sh script to do post install verification. This will basically run curl to get a get request on http://localhost:8000 and check for a 200 response from the webserver. If it fails, we'll get an error from the script, which we can see from the vagrant logs.

### Run this sample

First, make sure to have Vagrant and git installed locally. Then just:

```
git clone https://github.com/angelga/puppetlabs_hw.git ~/github/puppetlabs_sample
cd ~/github/puppetlabs_sample
vagrant up
```

That's it. You should see the Vagrant VM come up. On your browser, open this site [http://localhost:8080/](http://localhost:8000/).
