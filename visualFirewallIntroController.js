angular.module("visualFirewallApp").controller("visualFirewallIntroController", visualFirewallIntroController);

function visualFirewallIntroController($scope, $window, firewallVM) {
    var vm =
    {
        speed: null,
        whitelistIP: null,
        whiteList: [],
        saveSpeed: saveSpeed,
        addIpToWhitelist: addIpToWhitelist,
        checkSpeed: checkSpeed,
        removeFromWhitelist: removeFromWhitelist

    };

    init();

    function init() {

        $scope.vm = vm;
    }

    //Saving speed to the Service or App.
    function saveSpeed() {
        firewallVM.setSpeed(vm.speed);
    }

    //Pushing the IPs to the global list.
    function addIpToWhitelist() {
        if (vm.whitelistIP != null) {
            firewallVM.addIpToWhitelist(vm.whitelistIP);
            vm.whiteList.push(vm.whitelistIP);
            vm.whitelistIP = null;
        }
        
    }
    //Function to make sure you cannot continue with a null speed.
    function checkSpeed() {
        if (firewallVM.getSpeed() != null) {
            return true;
        } else {
            return false;
        }
    }
    //Function to delete from whitelist IP table.
    function removeFromWhitelist(IP) {
        var index = vm.whiteList.indexOf(IP);
        vm.whiteList.splice(index, 1);
        firewallVM.removeFromWhitelist(IP);
    }
}