Name:           ros-jade-ros-control-boilerplate
Version:        0.3.0
Release:        0%{?dist}
Summary:        ROS ros_control_boilerplate package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/davetcoleman/ros_control_boilerplate
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-actionlib
Requires:       ros-jade-control-msgs
Requires:       ros-jade-control-toolbox
Requires:       ros-jade-controller-manager
Requires:       ros-jade-hardware-interface
Requires:       ros-jade-joint-limits-interface
Requires:       ros-jade-ros-controllers
Requires:       ros-jade-roscpp
Requires:       ros-jade-rosparam-shortcuts
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-std-msgs
Requires:       ros-jade-trajectory-msgs
Requires:       ros-jade-transmission-interface
Requires:       ros-jade-urdf
BuildRequires:  gflags-devel
BuildRequires:  ros-jade-actionlib
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cmake-modules
BuildRequires:  ros-jade-control-msgs
BuildRequires:  ros-jade-control-toolbox
BuildRequires:  ros-jade-controller-manager
BuildRequires:  ros-jade-hardware-interface
BuildRequires:  ros-jade-joint-limits-interface
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-rosparam-shortcuts
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-trajectory-msgs
BuildRequires:  ros-jade-transmission-interface
BuildRequires:  ros-jade-urdf

%description
Simple simulation interface and template for setting up a hardware interface for
ros_control

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Mon Jan 04 2016 Dave Coleman <davetcoleman@gmail.com> - 0.3.0-0
- Autogenerated by Bloom

* Mon Dec 07 2015 Dave Coleman <davetcoleman@gmail.com> - 0.1.4-1
- Autogenerated by Bloom

* Mon Dec 07 2015 Dave Coleman <davetcoleman@gmail.com> - 0.1.4-0
- Autogenerated by Bloom

* Sat Dec 05 2015 Dave Coleman <davetcoleman@gmail.com> - 0.1.3-0
- Autogenerated by Bloom

