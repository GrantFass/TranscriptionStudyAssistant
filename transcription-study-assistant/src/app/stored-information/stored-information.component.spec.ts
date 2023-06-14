import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StoredInformationComponent } from './stored-information.component';

describe('StoredInformationComponent', () => {
  let component: StoredInformationComponent;
  let fixture: ComponentFixture<StoredInformationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StoredInformationComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(StoredInformationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
