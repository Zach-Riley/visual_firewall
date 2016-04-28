angular.module("visualFirewallApp").controller("visualFirewallIntroController", visualFirewallIntroController);

function visualFirewallIntroController($scope, $window, firewallVM) {
    var vm =
    {
        speed: null,
        whitelistIP: null,
        whiteList: [],
        saveSpeed: saveSpeed,
        addIpToWhitelist: addIpToWhitelist,
        checkSpeed: checkSpeed

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

    function getWhitelistedIPs() {
       vm.whiteList = firewallVM.getWhitelist();
    }
}