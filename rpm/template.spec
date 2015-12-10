Name:           ros-indigo-ros-control-boilerplate
Version:        0.2.1
Release:        0%{?dist}
Summary:        ROS ros_control_boilerplate package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/davetcoleman/ros_control_boilerplate
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-control-msgs
Requires:       ros-indigo-control-toolbox
Requires:       ros-indigo-controller-manager
Requires:       ros-indigo-hardware-interface
Requires:       ros-indigo-joint-limits-interface
Requires:       ros-indigo-ros-controllers
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-trajectory-msgs
Requires:       ros-indigo-transmission-interface
Requires:       ros-indigo-urdf
BuildRequires:  gflags-devel
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-control-msgs
BuildRequires:  ros-indigo-control-toolbox
BuildRequires:  ros-indigo-controller-manager
BuildRequires:  ros-indigo-hardware-interface
BuildRequires:  ros-indigo-joint-limits-interface
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-trajectory-msgs
BuildRequires:  ros-indigo-transmission-interface
BuildRequires:  ros-indigo-urdf

%description
Simple simulation interface and template for setting up a hardware interface for
ros_control

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Dec 09 2015 Dave Coleman <davetcoleman@gmail.com> - 0.2.1-0
- Autogenerated by Bloom

* Wed Dec 09 2015 Dave Coleman <davetcoleman@gmail.com> - 0.2.0-0
- Autogenerated by Bloom

* Mon Dec 07 2015 Dave Coleman <davetcoleman@gmail.com> - 0.1.3-0
- Autogenerated by Bloom

