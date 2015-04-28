Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
   
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provisioning/local.yml"
  end

  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.synced_folder "./blog", "/home/vagrant/www/website"

end
