import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PageResultatRechercheComponent } from './page-resultat-recherche.component';

describe('PageResultatRechercheComponent', () => {
  let component: PageResultatRechercheComponent;
  let fixture: ComponentFixture<PageResultatRechercheComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PageResultatRechercheComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PageResultatRechercheComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
