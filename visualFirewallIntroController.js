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

    function saveSpeed() {
        firewallVM.setSpeed(vm.speed);
    }

    function addIpToWhitelist() {
        if (vm.whitelistIP != null) {
            firewallVM.addIpToWhitelist(vm.whitelistIP);
            vm.whiteList.push(vm.whitelistIP);
            vm.whitelistIP = null;
        }
        
    }
    function checkSpeed() {
        if (firewallVM.getSpeed() != null) {
            return true;
        } else {
            return false;
        }
    }
    function removeFromWhitelist(IP) {
        var index = vm.whiteList.indexOf(IP);
        vm.whiteList.splice(index, 1);
        firewallVM.removeFromWhitelist(IP);
    }
}